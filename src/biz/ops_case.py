import json
from src.biz.dao import dao_case
import src.utils.comm as comm
from src.utils.enum import exec_status


class CaseMatch:
    _source_sql = ''
    _source_connect_id = 0
    _destination_sql = ''
    _destination_connect_id = 0
    _test_case_type = ''
    _threshlod_low = 0
    _threshlod_high = 0
    _duration_limit = 0

    def __init__(self, case_params):
        self._source_sql = case_params[0]
        self._source_connect_id = case_params[1] if case_params[1] is not None else 0
        self._destination_sql = case_params[2]
        self._destination_connect_id = case_params[3] if case_params[3] is not None else 0
        self._test_case_type = case_params[4]
        self._threshlod_low = case_params[5]
        self._threshlod_high = case_params[6]
        self._duration_limit = case_params[7]


class ExactlyMatch(CaseMatch):
    def __init__(self, case_params):
        CaseMatch.__init__(self, case_params)

    def RunCase(self):
        # step 1 Init
        current_status = exec_status.FAILED
        source_list = dao_case.get_list(
            self._source_connect_id, self._duration_limit, self._source_sql)
        target_list = dao_case.get_list(
            self._destination_connect_id, self._duration_limit, self._destination_sql)
        source_result = json.dumps(source_list)
        target_result = json.dumps(target_list)
        source_set = set(source_list)
        target_set = set(target_list)
        # step 2 duplicate data checking
        if len(source_list) > len(source_set):
            diff = "Source total count:{0}, distinct count:{1}".format(
                len(source_list), len(source_set))
            result_message = "Source side data is duplicate"
            return current_status, diff, result_message, source_result, target_result
        if len(target_list) > len(target_set):
            diff = "Target total count:{0}, distinct count:{1}".format(
                len(target_list), len(target_set))
            result_message = "Target side data is duplicate"
            return current_status, diff, result_message, source_result, target_result
        # step 3 compare the diff between source and target
        source_diff = source_set - target_set
        target_diff = target_set - source_set
        if(len(source_diff) == 0 and len(target_diff) == 0):
            current_status = exec_status.SUCCESS
            diff = ""
            result_message = "Source is totally matched with target --> Source count:{0},target count:{1}".format(
                len(source_list), len(target_list))
            return current_status, diff, result_message, source_result, target_result
        _diff = {
            "source-target": list(source_diff),
            "target-source": list(target_diff)
        }
        diff = json.dumps(_diff)
        result_message = "Source is not matched with target"
        return current_status, diff, result_message, source_result, target_result


class RangeMatch(CaseMatch):
    def __init__(self, case_params):
        CaseMatch.__init__(self, case_params)

    def RunCase(self):
        current_status = exec_status.FAILED
        source_result = ""
        target_result = ""
        diff = ""
        result_message = "execution is not success"

        if (self._source_connect_id > 0 and self._destination_connect_id == 0):
            source_count = dao_case.get_one(
                self._source_connect_id, self._duration_limit, self._source_sql)
            source_num = comm.int_val(source_count[0])
            if(len(source_count) > 0 and source_num is not None):
                source_result = source_num
                if(source_num >= self._threshlod_low and source_num <= self._threshlod_high):
                    current_status = exec_status.SUCCESS
                    result_message = "The value:{0} is in range".format(
                        source_num)
                else:
                    diff = "The value:{0} not in range".format(source_num)

        elif(self._source_connect_id == 0 and self._destination_connect_id > 0):
            target_count = dao_case.get_one(
                self._destination_connect_id, self._duration_limit, self._destination_sql)
            target_num = comm.int_val(target_count[0])
            if(len(target_count) > 0 and target_num is not None):
                target_result = target_num
                if(target_num >= self._threshlod_low and target_num <= self._threshlod_high):
                    current_status = exec_status.SUCCESS
                    result_message = "The value:{0} is in range".format(
                        target_num)
                else:
                    diff = "The value:{0} not in range".format(target_num)

        elif(self._source_connect_id > 0 and self._destination_connect_id > 0):
            source_count = dao_case.get_one(
                self._source_connect_id, self._duration_limit, self._source_sql)
            target_count = dao_case.get_one(
                self._destination_connect_id, self._duration_limit, self._destination_sql)
            if(len(source_count) > 0 and len(target_count) > 0):
                source_result = source_num
                target_result = target_num
                source_num = comm.int_val(source_count[0])
                target_num = comm.int_val(target_count[0])
                if(source_num is not None and target_num is not None):
                    gap_num = abs(source_num - target_num)
                    if(gap_num >= self._threshlod_low and gap_num <= self._threshlod_high):
                        current_status = exec_status.SUCCESS
                        result_message = "The value:{0} is in range".format(
                            gap_num)
                    else:
                        diff = "source_num:{0} - target_num:{1} = {2} not in range".format(
                            source_num, target_num, gap_num)

        return current_status, diff, result_message, source_result, target_result
