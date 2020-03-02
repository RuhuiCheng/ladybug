from pyhive import hive


def get_conn(hive_host, hive_port, hive_user, hive_password, hive_database, timeout=None):
    return hive.Connection(
        host=hive_host,
        port=hive_port,
        username=hive_user,
        password=hive_password,
        database=hive_database,
        socket_timeout=timeout*1000,
        auth='LDAP'
    )


def get_list(conn, sql_text):
    res = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
            res = cursor.fetchall()
    finally:
        conn.close()
    return res

def get_one(conn, sql_text):
    res = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
            res = cursor.fetchone()
    finally:
        conn.close()
    return res