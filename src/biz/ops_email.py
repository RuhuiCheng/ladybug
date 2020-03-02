from src.plugin import email
from jinja2 import Template


def send_kpi_mail(ls_kpi):
    if ls_kpi is None:
        return True
    if len(ls_kpi) == 0:
        return True
    mail_subject = ls_kpi[0][1]
    mail_msg = ls_kpi[0][2]
    ls_to = ls_kpi[0][3].split(',')
    ls_cc = None
    ls_bcc = None
    if ls_kpi[0][4] is not None:
        ls_cc = ls_kpi[0][4].split(',')
    if ls_kpi[0][5] is not None:
        ls_bcc = ls_kpi[0][5].split(',')

    ls_th = []
    ls_td = []
    for item in ls_kpi:
        ls_th.append(item[6])
        item_value = ''
        if len(item[8]) > 0 and len(item[9]) == 0:
            item_value = item[8]
        elif len(item[8]) == 0 and len(item[9]) > 0:
            item_value = item[9]
        elif len(item[8]) > 0 and len(item[9]) > 0:
            item_value = item[10]
        ls_td.append(item_value)
    template = Template(mail_msg)
    mail_msg = template.render(ls_th=ls_th, ls_td=ls_td)
    bl = email.send(ls_to, ls_cc, ls_bcc, mail_subject, mail_msg)
    return bl


def send_failed_mail(ls_failed):
    if ls_failed is None:
        return True
    if len(ls_failed) == 0:
        return True
    mail_subject = ls_failed[0][1]
    mail_msg = ls_failed[0][2]
    ls_to = ls_failed[0][3].split(',')
    if ls_kpi[0][4] is not None:
        ls_cc = ls_kpi[0][4].split(',')
    if ls_kpi[0][5] is not None:
        ls_bcc = ls_kpi[0][5].split(',')
    template = Template(mail_msg)
    mail_msg = template.render(ls_failed=ls_failed)
    bl = email.send(ls_to, ls_cc, ls_bcc, mail_subject, mail_msg)
    return bl
