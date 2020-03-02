from src.api import case_email


def test_send_email():
    bl = case_email.send_email()
    assert bl