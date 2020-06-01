import json_utils
import test_data_prep
import datetime


def pre_test(json_data, modifications):
    change_from = 'AAA'

    # Do a recursive search and replace into test item
    if json_utils.is_string_valid(modifications['change_to']):
        json_utils.testcase_srch_replace(change_from, modifications['change_to'], json_data)
    else:
        pass

    tester_data = test_data_prep.get_tester_data()  # pre_test.tester_data is now static variable during process (obsolete now)

    for item in json_data:
        item['testheader']['rundatetime'] = json_utils.json_serial(datetime.datetime.now())
        item['testheader']['tester'] = tester_data['testerid']
        item['testheader']['test_run_id'] = tester_data['testrunid']

    return json_data


# Modify and add these, if you do want some new data specific manipulation
def pre_loc(json_data, modifications):
    return pre_test(json_data, modifications)


def pre_poc(json_data, modifications):
    return pre_test(json_data, modifications)


def pre_bulk(json_data, modifications):
    return pre_test(json_data, modifications)


def pre_city_nature(json_data, modifications=None):
    for item in json_data:
        for field in modifications['del_keys']:
            del item[field]
    return json_data