import smtplib
import logging
from email.mime.text import MIMEText
from email.header import Header
from src.utils import conf
logger = logging.getLogger(__name__)


def send(ls_to, ls_cc, ls_bcc, mail_subject, mail_msg):
    config = conf.init()
    msg = MIMEText(mail_msg, 'html', 'utf-8')
    msg['From'] = Header(config.mail_sender, 'utf-8')
    msg['To'] = Header(",".join(str(i) for i in ls_to), 'utf-8')
    receivers = ls_to
    if ls_cc is not None:
        msg['Cc'] = Header(",".join(str(i) for i in ls_cc), 'utf-8')
        receivers = receivers + ls_cc
    if ls_bcc is not None:
        msg['Bcc'] = Header(",".join(str(i) for i in ls_bcc), 'utf-8')
        receivers = receivers + ls_bcc
    msg['Subject'] = Header(mail_subject, 'utf-8')
    bl_status = False
    try:
        smtp = smtplib.SMTP_SSL("{0}:{1}".format(config.mail_host, config.mail_port))
        # smtp.connect(config.mail_host, config.mail_port)   # 25 为 SMTP 端口号
        smtp.login(config.mail_user, config.mail_password)
        smtp.sendmail(config.mail_sender, receivers, msg.as_string())
        bl_status = True
    except smtplib.SMTPException as e:
        logger.exception(
            'error happened in send trace-->{0}'.format(e))
    finally:
        smtp.close()
    return bl_status
