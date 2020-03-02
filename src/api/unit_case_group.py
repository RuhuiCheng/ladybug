import time
import logging
from src.biz.dao import dao_execution, dao_case_group
import src.api.unit_case as unit_case
from src.utils.enum import exec_status
logger = logging.getLogger(__name__)


def run_case_group(group_name, execution_id=-1):
    logger.info("group_name:{0} running start.".format(group_name))
    # step 1 get case list by group
    ls_case = dao_case_group.get_case_by_group(group_name)
    if ls_case is None:
        logger.info(
            "group_name:{0} is disabled or not exist".format(group_name))
        return

    # step 2 Init group execution
    is_group_run = 0
    if execution_id == -1:
        is_group_run = 1
        execution_type = 'TaskGroup'
        execution_name = group_name
        execution_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        execution_id = dao_execution.add_task_execution(
            execution_type, execution_name, execution_start)

    # step 3 run case list in the current group
    try:
        failed_count = 0
        for task_case in ls_case:
            case_name = task_case[0]
            response = unit_case.run_case(case_name, execution_id)
            if response is None or response[0] is exec_status.FAILED:
                failed_count = failed_count + 1
    except Exception as e:
        logger.exception(
            'run_case_group error case group name-->{0} trace-->{1}'.format(group_name, e))

    # step 4 update group execution
    current_status = exec_status.SUCCESS
    if failed_count > 0:
        current_status = exec_status.FAILED
    if is_group_run == 1:
        execution_end = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())
        dao_execution.update_task_execution(
            execution_id, current_status, execution_end)
    # step 5 return the group exec status
    logger.info("group_name:{0} running done.".format(group_name))
    return current_status, execution_id
