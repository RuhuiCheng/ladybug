import logging
import src.utils.log
import src.api.unit_case as unit_case


def test_demo1():
    res = unit_case.run_case('kpi.agreement_overlap_check.hotel_count')
    assert res is not None

def test_demo2():
    res = unit_case.run_case('demo2')
    assert res is not None

def test_demo3():
    res = unit_case.run_case('demo3')
    assert res is not None
