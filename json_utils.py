# Utilities to complete test set data
from datetime import date, datetime

# from robot.api import logger


ROBOT_FRAMEWORK_ENV = False


# For future use, logging encapsulated so you can remove robot.api imports
# in case Robot Framework will not/cannot be used
def log_exceptions(log_out):
    global ROBOT_FRAMEWORK_ENV
    if ROBOT_FRAMEWORK_ENV:
        pass  # logger.console(log_out)
    else:  # usage from command line, another python library etc.
        print(log_out)


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def is_string_valid(my_string):
    if my_string is None:
        return False
    if "".__eq__(my_string):
        return False
    return True


# Recursively replace Python dictionary
def testcase_srch_replace(pattern, replacestring, key):
    if isinstance(key, dict):
        for k in key:
            if key[k] and isinstance(key[k], str):
                key[k] = key[k].replace(pattern, replacestring)
            elif (key[k], dict):
                testcase_srch_replace(pattern, replacestring, key[k])
    elif isinstance(key, list):
        for item in key:
            testcase_srch_replace(pattern, replacestring, item)
