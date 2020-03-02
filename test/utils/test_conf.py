from src.utils import conf

def test_conf():
    obj = conf.init()
    assert obj is not None