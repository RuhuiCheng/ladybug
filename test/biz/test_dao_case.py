from src.biz.dao import dao_case

def test_get_case_config():
    res = dao_case.get_case_config('oyo_dw-demo1')
    assert res is not None