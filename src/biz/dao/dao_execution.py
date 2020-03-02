import src.db.db_mysql as cli_mysql
from src.biz.dao import dao_conn
from src.utils.enum import exec_status


def add_task_execution(execution_type, execution_name, execution_start):
    row_id = None
    conn = dao_conn.get_metadata_conn()
    sql_text = "INSERT INTO task_execution\
                (execution_type, execution_name, current_status, execution_start)\
                VALUES('{0}', '{1}', '{2}', '{3}')".format(execution_type, execution_name, exec_status.PROCESSING.name, execution_start)
    row_id = cli_mysql.execute_one(conn, sql_text)
    return row_id


def update_task_execution(execution_id, current_status, execution_end):
    _status = exec_status(current_status)
    conn = dao_conn.get_metadata_conn()
    sql_text = "UPDATE task_execution\
        SET current_status='{0}', execution_end='{1}', update_date=CURRENT_TIMESTAMP\
        WHERE id={2}".format(_status.name, execution_end, execution_id)
    cli_mysql.execute_one(conn, sql_text)
