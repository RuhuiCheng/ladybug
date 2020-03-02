import logging
from src.db import db_mysql, db_hive, db_oracle
from src.utils import conf
from src.utils.enum import db_conn
logger = logging.getLogger(__name__)
db_list = None


def get_metadata_conn():
    config = conf.init()
    conn = db_mysql.get_conn(config.mysql_host, config.mysql_port,
                             config.mysql_user, config.mysql_password, config.mysql_database)
    return conn


def __conn_metadata():
    sql_text = 'select id,db_connect_type,host,port,username,password,db_name from db_connect'
    try:
        conn = get_metadata_conn()
        res = db_mysql.get_list(conn, sql_text)
        return res
    except Exception as e:
        logger.exception(
            'Init conn_metadata() error sql-->{0} trace-->{1}'.format(sql_text, e))


def get_conn(conn_id, duration_limit):
    global db_list
    if db_list is None:
        db_list = __conn_metadata()

    conn = None
    conn_type = None
    item = [i for i in db_list if i[0] == conn_id]
    if len(item) > 0:
        conn_type = item[0][1]
        pwd = None
        if len(item[0][5].strip()) > 0:
            pwd = item[0][5]
        
        if conn_type == db_conn.HIVE.value:
            conn = db_hive.get_conn(item[0][2], item[0][3], item[0]
                                    [4], pwd, item[0][6], duration_limit)
        elif conn_type == db_conn.MYSQL.value:
            conn = db_mysql.get_conn(item[0][2], item[0][3], item[0]
                                     [4], pwd, item[0][6], duration_limit)
        elif conn_type == db_conn.ORACLE.value:
            conn = db_oracle.get_conn(item[0][2], item[0][3], item[0]
                                      [4], pwd, item[0][6], duration_limit)
    return conn, conn_type
