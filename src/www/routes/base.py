import logging
from flask import Blueprint, request
boot = Blueprint('main', __name__)
logger = logging.getLogger(__name__)


@boot.route('/ping', methods=['GET'])
def health_check():
    return 'pong'


"""
Use MQ to refine the processing 
1. more flexable 
2. more performance
"""
@boot.route('/', methods=['GET', 'POST'])
def run_case():
    try:
        case_type, = request.values
        unit_name, = request.values.values()
        logger.info("The case type:{0},name:{1}".format(case_type, unit_name))
    except Exception as e:
        logger.exception(
            'run_case error trace-->{0}'.format(e))
