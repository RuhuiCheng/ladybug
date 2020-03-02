import cx_Oracle
import logging
logger = logging.getLogger(__name__)


def get_conn(oracle_host, oracle_port, oracle_user, oracle_password, oracle_database, timeout=None):
    conn = cx_Oracle.connect(oracle_user, oracle_password,
                             '{0}:{1}/{2}'.format(oracle_host, oracle_port, oracle_database))
    conn.callTimeout = timeout*1000
    return conn


def get_list(conn, sql_text):
    logger.info(sql_text)
    res = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
            res = cursor.fetchall()
    finally:
        conn.close()
    return res


def get_one(conn, sql_text):
    logger.info(sql_text)
    res = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
            res = cursor.fetchone()
    finally:
        conn.close()
    return res
