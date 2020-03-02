import src.db.db_hive as db_hive
from src.biz.dao import dao_conn


def test_get_list():
    sql_text = 'select reflect("java.lang.Thread", "sleep", bigint(15000)) as c1, 1 as c2'
    conn = dao_conn.get_conn(1, 60)
    result = db_hive.get_list(sql_text)
    assert result is not None
