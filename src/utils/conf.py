from src.utils import ucm
cfg = None
import logging

class Config:
    # log
    log_path = '/data/logs/bigdata-dq'
    log_level = 'INFO'
    # smtp server
    mail_host = 'smtp.ladybughotels.cn'
    # smtp port
    mail_port = 465
    # smtp_user
    mail_user = 'bigdata@ladybughotels.cn'
    # smtp_password
    mail_password = 'ladybug123ladybug'
    # mail_sender
    mail_sender = 'bigdata@ladybughotels.cn'


class PRDConfig(Config):
    # mysql metadata
    mysql_host = 'ladybug-dev-database.mysql.rds.aliyuncs.com'
    mysql_port = 3306
    mysql_user = 't_data_quality_1'
    mysql_password = 'gdeESFxmiZf31YIQ$@b0'
    mysql_database = 'data_quality'


class DEVConfig(Config):
    # Basic info
    log_level = 'INFO'
    # log_path = '/data/logs/bigdata-dq'
    log_path = '/Users/ladybug04316/Documents/repo/bigdata-dq/log'
    # QQ mail
    mail_host = 'smtp.qq.com'
    mail_port = 465
    mail_user = '55259362@qq.com'
    mail_password = 'jkqyfgqyylhlbige'
    mail_sender = '55259362@qq.com'
    # mysql metadata
    mysql_host = 'localhost'
    mysql_port = 3306
    mysql_user = 'root'
    mysql_password = '123456'
    mysql_database = 'data_quality'

def init():
    global cfg
    if cfg is not None:
        return cfg
    __envs = {
        'dev': DEVConfig,
        'test': DEVConfig,
        'uat': PRDConfig,
        'pro': PRDConfig,
        'default': DEVConfig
    }
    __default_env = "default"
    env, ls_url = ucm.get_server_properties()
    if env:
        env = env.lower()
        if env in __envs:
            __default_env = env
    cfg = __envs[__default_env]
    # if cfg is DEVConfig:
    #     return cfg
    conn = ucm.get_metadata_dbinfo(ls_url)
    # print(">>>>>>>>>> conn=%s" % conn)
    cfg.mysql_host = conn.get('host')
    cfg.mysql_port = int(conn.get('port'))
    cfg.mysql_user = conn.get('user')
    cfg.mysql_password = conn.get('password')
    cfg.mysql_database = conn.get('database')
    return cfg
