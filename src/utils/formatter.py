import logging
import json
from src.utils.ucm import app_id, env


class JsonLogFormatter(logging.Formatter):

    def format(self, record):
        msg = ''
        if record.exc_text is None:
            msg = record.message
        else:
            msg = record.exc_text
        data = {
            'app_id': ''+app_id+'',
            'asctime': ''+record.asctime+'',
            'env': ''+env+'',
            'file_name': ''+record.filename+'',
            'func_name': ''+record.funcName+'',
            'level': ''+record.levelname+'',
            'line_number': record.lineno,
            'message': ''+msg+''
        }
        string_msg = json.dumps(data)
        return string_msg
