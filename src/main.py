import logging
import src.utils.log
from sys import argv
from src.api import unit_case, unit_case_group, unit_case_scenarios
from src.api import case_email, case_email_group, case_email_scenarios
from src.utils.enum import case_category
logger = logging.getLogger(__name__)


def run(case_type, unit_name):
    bl = True
    try:
        case_type = case_type.upper()
        if case_type == case_category.CASE.name:
            unit_case.run_case(unit_name)
            case_email.send_email(unit_name)
        elif case_type == case_category.GROUP.name:
            unit_case_group.run_case_group(unit_name)
            case_email_group.send_email(unit_name)
        elif case_type == case_category.SCENARIOS.name:
            unit_case_scenarios.run_case_scenarios(unit_name)
            case_email_scenarios.send_email(unit_name)
        else:
            bl = False
            logger.info("case type: is not valid")
    except Exception as e:
        bl = False
        logger.exception(
            "run error case_type:{0} unit_name:{1} trace-->{2}".format(case_type, unit_name, e))
    return bl


def __setup_param():
    if len(argv) == 2:
        if argv[1] != '-h':
            if argv[1].find('=') > 0:
                case_type, case_name = argv[1].split('=')
                return case_type, case_name
    logger.info("-----------------------------------------")
    logger.info("please follow the below pattern.")
    logger.info("-----------------------------------------")
    logger.info("ladybug case=case_name")
    logger.info("ladybug group=group_name")
    logger.info("ladybug scenarios=scenarios_name")
    logger.info("-----------------------------------------")


if __name__ == "__main__":
    param = __setup_param()
    if param is not None:
        run(param[0], param[1])
