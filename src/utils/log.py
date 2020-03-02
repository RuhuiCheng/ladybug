import os
import logging
import logging.config
from src.utils import conf

def log_init():
    config = conf.init()
    log_dir = config.log_path
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, "app.log")
    _log_setup = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "class": "src.utils.formatter.JsonLogFormatter"
            },
            "standard": {
                "format": "%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "simple",
                "filename": log_file,
                "mode": "w+",
                "maxBytes": 1024*1024*1024,  # 1G
                "backupCount": 14,
                "encoding": "utf8"
            }
        },
        "root": {
            "handlers": ["console", "file"],
            "level": config.log_level,
            "propagate": False
        }
    }
    logging.config.dictConfig(_log_setup)


log_init()
