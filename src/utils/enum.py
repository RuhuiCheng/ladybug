from enum import IntEnum, unique


class exec_status(IntEnum):
    FAILED = 0
    SUCCESS = 1
    PROCESSING = 2


@unique
class db_conn(IntEnum):
    HIVE = 1
    MYSQL = 2
    ORACLE = 3


@unique
class case_category(IntEnum):
    CASE = 1
    GROUP = 2
    SCENARIOS = 3


@unique
class match_type(IntEnum):
    EXACTLY = 1
    RANGE = 2


@unique
class email_type(IntEnum):
    KPI = 1
    FAILED = 2
