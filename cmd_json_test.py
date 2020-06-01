import json
import datetime
import sys
import argparse

import test_validations
import json_file_operations
import test_cases


pattern_change_to = "_PYTHON entry_"


def run_regression():
    modifications = {'change_to': pattern_change_to, 'del_keys': ['routes', 'points']}
    for test in test_cases.regression_tests:
        try:
            testset = test_validations.json_validation(test, modifications)
        except ValueError:
            print('Test case: ' + test['test_name'] + ' failed')
            raise ValueError
        else:
            print_testset_in_json(testset)

    # Just for demonstration, write the last test set into files with json and yaml format
    json_file_operations.write_python_to_yaml_file('testing_out.yaml', testset)
    json_file_operations.write_python_to_json_file('testing_out.json', testset)


def print_testset_in_json(test_run):
    print('\n------------------------ Test data dump in json -------------------------')
    json_string = json.dumps(test_run, sort_keys=False, indent=4, ensure_ascii=False)
    print(json_string)


def main(arguments):
    parser = argparse.ArgumentParser(usage="python cmd_json_test.py")
    parser.parse_args()

    start_time = datetime.datetime.now()
    try:
        run_regression()
    except ValueError:
        return 1
    end_time = datetime.datetime.now()

    elapsed_time = end_time - start_time
    elapsed_seconds = elapsed_time.total_seconds()


    print("\nElapsed time " + str(elapsed_seconds) + " Seconds")
    print("\n//////////////////// Data is validated O.K with schema ////////////////////")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
