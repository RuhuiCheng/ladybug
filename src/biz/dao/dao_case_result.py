import src.db.db_mysql as cli_mysql
from src.biz.dao import dao_conn
from src.utils.enum import exec_status


def add_task_result(task_case_id, task_execution_id, execution_start):
    row_id = None
    conn = dao_conn.get_metadata_conn()
    sql_text = "INSERT INTO task_case_result\
                (task_case_id, task_execution_id, current_status, execution_start)\
                VALUES({0},{1}, '{2}', '{3}')".format(task_case_id, task_execution_id, exec_status.PROCESSING.name, execution_start)
    row_id = cli_mysql.execute_one(conn, sql_text)
    return row_id


def update_task_result(case_result_id, current_status, execution_end, diff, result_message, source_result, target_result):
    _status = exec_status(current_status)
    conn = dao_conn.get_metadata_conn()
    sql_text = "UPDATE task_case_result\
                SET current_status='{0}', execution_end='{1}', diff='{2}', result_message='{3}', source_result = '{5}', destination_result = '{6}',\
                update_date=CURRENT_TIMESTAMP\
                WHERE id={4}".format(_status.name, execution_end, diff, result_message, case_result_id, source_result, target_result)
    cli_mysql.execute_one(conn, sql_text)


def get_task_result(sql_text):
    conn = dao_conn.get_metadata_conn()
    res = cli_mysql.get_list(conn, sql_text)
    return res
