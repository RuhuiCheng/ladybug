import time
import logging
from src.biz.dao import dao_execution, dao_case_scenarios
import src.api.unit_case_group as unit_case_group
from src.utils.enum import exec_status
logger = logging.getLogger(__name__)


def run_case_scenarios(scenarios_name):
    logger.info("scenarios_name:{0} running start.".format(scenarios_name))
    # step 1 get group list by scenarios_name
    ls_group = dao_case_scenarios.get_group_by_scenarios(scenarios_name)
    if ls_group is None:
        logger.info(
            "scenarios_name:{0} is disabled or not exist".format(scenarios_name))
        return

    # step 2 Init scenarios execution
    execution_type = 'TaskScenarios'
    execution_name = scenarios_name
    execution_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    execution_id = dao_execution.add_task_execution(
        execution_type, execution_name, execution_start)

    # step 3 run group list in the current scenarios
    try:
        failed_count = 0
        for task_group in ls_group:
            group_name = task_group[0]
            response = unit_case_group.run_case_group(group_name, execution_id)
            if (response is None) or (response[0] is exec_status.FAILED):
                failed_count = failed_count + 1
    except Exception as e:
        logger.exception(
            'run_case_scenarios error case group name-->{0} trace-->{1}'.format(group_name, e))

    # step 4 update group execution
    current_status = exec_status.SUCCESS
    if failed_count > 0:
        current_status = exec_status.FAILED

    execution_end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dao_execution.update_task_execution(
        execution_id, current_status, execution_end)
    # step 5 return the scenarios exec status
    logger.info("scenarios_name:{0} running done.".format(scenarios_name))
    return current_status, execution_id
