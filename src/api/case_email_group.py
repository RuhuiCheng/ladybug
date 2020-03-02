from src.biz import ops_email
from src.biz.dao import dao_case_result
from src.utils.enum import email_type, exec_status

import logging
logger = logging.getLogger(__name__)

def get_email_data(group_name):
    sql_text ="SELECT  e.id,e.email_subject,e.msg_template,e.email_to,e.email_cc,e.email_bcc\
                ,t.alias\
                ,r.current_status, r.source_result, r.destination_result, r.diff, r.result_message\
                ,o.name\
                FROM task_case_result as r\
                inner join (select max(id) as rid  FROM task_case_result\
							where date(update_date) >= DATE_SUB(curdate(),INTERVAL 1 DAY)\
							group by task_case_id ) as tcr on r.id = tcr.rid\
                inner join task_case as t\
                on r.task_case_id = t.id\
                inner join case_group as cg\
                on t.id = cg.task_case_id\
                inner join task_group as tg\
                on cg.task_group_id  = tg.id\
                inner join email_template as e\
                on t.email_template_id = e.id\
                inner join user as o\
                on t.owner_id = o.id\
                where t.is_enabled = 1\
                and tg.is_enabled = 1\
                and tg.task_group_name = '{0}'".format(group_name)
    res = dao_case_result.get_task_result(sql_text)
    ls_kpi = [i for i in res if i[1] == email_type.KPI.name]
    ls_failed = [i for i in res if (i[1] == email_type.FAILED.name and i[7] == exec_status.FAILED.name)]
    return ls_kpi,ls_failed

def send_email(group_name):
    bl = False
    try:
        ls_kpi,ls_failed = get_email_data(group_name)
        # 1 send daily kpi of last day
        logger.info("1 send daily kpi of last day")
        bl = ops_email.send_kpi_mail(ls_kpi)
        # 2 send failed test case of last day
        logger.info("2 send failed test case of last day")
        bl = ops_email.send_failed_mail(ls_failed)
    except Exception as e:
        logger.exception('send_email error trace-->{0}'.format(e))
    return bl
