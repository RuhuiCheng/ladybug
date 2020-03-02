import logging
import time
from src.biz import ops_case
from src.biz.dao import dao_case, dao_case_result
from src.utils.enum import match_type
from src.utils.enum import exec_status
logger = logging.getLogger(__name__)


def run_case(case_name, execution_id=-1):
    try:
        current_status, exec_end, diff, result_message, source_result, target_result = "FAILED","","","","",""
        try:
            logger.info("case_name:{0} running start.".format(case_name))
            case_params = dao_case.get_case_config(case_name)
            if case_params is None:
                logger.info(
                    "case_name:{0} is disabled or not exist".format(case_name))
                return
            case_type = case_params[4]
            case_id = case_params[8]
            # step 1 case result data init
            exec_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            result_id = dao_case_result.add_task_result(
                case_id, execution_id, exec_start)
            if result_id is None:
                logger.error(
                    "case_name:{0} failed in add_task_result() step".format(case_name))
                return
        except Exception as e:
            logger.exception(
                'run_case error case name-->{0} trace-->{1}'.format(case_name, e))
            return

        # step 2 run test case
        cli = None
        if case_type == match_type.EXACTLY.value:
            cli = ops_case.ExactlyMatch(case_params)
        elif case_type == match_type.RANGE.value:
            cli = ops_case.RangeMatch(case_params)
        if cli is None:
            logger.error("case_type:{0} is not exists".format(case_type))
            return
        response = cli.RunCase()
        if response is None:
            logger.error(
                "case_name:{0} failed in RunCase() step".format(case_name))
            return
        # step 3 update case
        current_status = response[0]
        exec_end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        diff = response[1]
        result_message = response[2]
        source_result = response[3]
        target_result = response[4]
        dao_case.update_case(case_id, result_id,
                             current_status, exec_end, diff, result_message, source_result, target_result)
        logger.info("case_name:{0} running done.".format(case_name))

        return current_status, result_id
    except Exception as e:
        current_status = exec_status.FAILED
        exec_end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        diff = "error happend"
        result_message = str(e)
        dao_case.update_case(case_id, result_id,
                             current_status, exec_end, diff, result_message, source_result, target_result)
        logger.exception(
            'run_case error case name-->{0} trace-->{1}'.format(case_name, e))
