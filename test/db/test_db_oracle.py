import logging
import src.utils.log
from src.db import db_oracle
logger = logging.getLogger(__name__)


def test_get_list():
    try:
        sql_text = 'SELECT 1 AS c1 FROM sys.dual'
        oracle_host = '10.200.71.247'
        oracle_port = 1521
        oracle_user = 'ladybug_dw'
        oracle_password = "eOD'F9A3q2m~om_tfCKz"
        oracle_database = 'ladybugdw'
        timeout = 60
        logger.info("get conn")
        conn = db_oracle.get_conn(
            oracle_host, oracle_port, oracle_user, oracle_password, oracle_database, timeout)
        logger.info("get list")
        res = db_oracle.get_list(conn, sql_text)
        logger.info(res)
        logger.info("done......")
        assert res
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    test_get_list()