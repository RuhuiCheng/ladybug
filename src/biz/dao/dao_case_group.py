import src.db.db_mysql as cli_mysql
from src.biz.dao import dao_conn


def get_case_by_group(group_name):
    sql_text = 'select tc.task_case_name\
                from task_group as tg\
                left join case_group as cg on tg.id = cg.task_group_id\
                left join task_case as tc on tc.id = cg.task_case_id\
                where tg.is_enabled = 1\
                  and tc.is_enabled = 1\
                  and tg.task_group_name = "{0}"'.format(group_name)
    conn = dao_conn.get_metadata_conn()
    res = cli_mysql.get_list(conn, sql_text)
    return res