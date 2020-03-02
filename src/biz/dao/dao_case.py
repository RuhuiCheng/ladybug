from src.db import db_mysql, db_hive, db_oracle
from src.biz.dao import dao_conn, dao_case_result
import src.utils.comm as comm
from src.utils.enum import db_conn


def get_case_config(case_name):
    sql_text = 'select id,task_case_name,source_sql,source_connect_id,destination_sql\
                ,destination_connect_id,match_type,threshlod_low,threshlod_high,duration_limit\
                from task_case WHERE is_enabled = 1 and task_case_name = "{0}"'.format(case_name)
    case_params = None
    conn = dao_conn.get_metadata_conn()
    res = db_mysql.get_one(conn, sql_text)
    if res is not None:
        case_params = (res[2], res[3], res[4],
                       res[5], res[6], res[7],
                       res[8], res[9], res[0])
    return case_params


def update_case(case_id, result_id, current_status, execution_end, diff, result_message, source_result, target_result):
    msg = comm.str_clear(result_message)
    # step 1 update case lastrun
    sql_text = 'UPDATE task_case SET last_run="{0}",\
                update_date=CURRENT_TIMESTAMP WHERE id={1}'.format(execution_end, case_id)
    conn = dao_conn.get_metadata_conn()
    db_mysql.execute_one(conn, sql_text)
    # step 2 update case result
    dao_case_result.update_task_result(
        result_id, current_status, execution_end, diff, msg, source_result, target_result)


def get_list(conn_id, duration_limit, sql_text):
    conn, conn_type = dao_conn.get_conn(conn_id, duration_limit)
    res = None
    if conn_type == db_conn.HIVE.value:
        res = db_hive.get_list(conn, sql_text)
    elif conn_type == db_conn.MYSQL.value:
        res = db_mysql.get_list(conn, sql_text)
    elif conn_type == db_conn.ORACLE.value:
        res = db_oracle.get_list(conn, sql_text)
    return res


def get_one(conn_id, duration_limit, sql_text):
    conn, conn_type = dao_conn.get_conn(conn_id, duration_limit)
    res = None
    if conn_type == db_conn.HIVE.value:
        res = db_hive.get_one(conn, sql_text)
    elif conn_type == db_conn.MYSQL.value:
        res = db_mysql.get_one(conn, sql_text)
    elif conn_type == db_conn.ORACLE.value:
        res = db_oracle.get_one(conn, sql_text)
    return res
