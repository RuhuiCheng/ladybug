from src.utils.enum import db_conn,case_category,match_type


def test_db_conn():
    try:
        txt = case_category.CASE.name
        print(txt)
    except Exception as e:
        print(e)
