import src.api.unit_case_scenarios as unit_case_scenarios


# run case scenarios
def test_ladybug_scenarios_demo1():
    res = unit_case_scenarios.run_case_scenarios("ladybug_scenarios_demo1")
    assert res is not None
