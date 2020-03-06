import logging
import src.utils.log
from src.db import db_hive
logger = logging.getLogger(__name__)


def test_get_list():
    try:
        sql_text = 'select CURRENT_DATE() as c1'
        hive_host = '10.203.0.54'
        hive_port = 10000
        hive_user = 'bigdata_etl'
        hive_password = 'internal'
        hive_database = 'ladybug_dw'
        timeout = 60
        logger.info("get conn")
        conn = db_hive.get_conn(
            hive_host, hive_port, hive_user, hive_password, hive_database, timeout)
        logger.info("get list")
        res = db_hive.get_list(conn, sql_text)
        logger.info(res)
        logger.info("done......")
        assert res
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    test_get_list()