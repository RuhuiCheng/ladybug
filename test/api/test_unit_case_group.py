import src.api.unit_case_group as unit_group


# run case group failed
def test_group_demo1():
    res = unit_group.run_case_group("group_demo1")
    assert res is not None


# run case group success
def test_group_demo2():
    res = unit_group.run_case_group("group_demo2")
    assert res is not None


# run case group success
def test_group_demo3():
    res = unit_group.run_case_group("group_demo3")
    assert res is not None
