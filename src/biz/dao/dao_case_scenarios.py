import src.db.db_mysql as cli_mysql
from src.biz.dao import dao_conn


def get_group_by_scenarios(scenarios_name):
    sql_text = "SELECT task_group_name\
                FROM task_scenarios as ts\
                left join group_scenarios as gs on ts.id = gs.task_scenarios_id\
                left join task_group as tg on tg.id = gs.task_group_id\
                where ts.is_enabled = 1\
                  and tg.is_enabled = 1\
                  and ts.task_scenarios_name = '{0}'".format(scenarios_name)
    conn = dao_conn.get_metadata_conn()
    res = cli_mysql.get_list(conn, sql_text)
    return res
