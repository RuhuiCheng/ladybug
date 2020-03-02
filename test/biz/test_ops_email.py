from src.biz import ops_email
from jinja2 import Template

def test_send_kpi_mail():
    bl =  ops_email.send_kpi_mail()
    assert bl


def test_send_failed_mail():
    bl =  ops_email.send_failed_mail()
    assert bl