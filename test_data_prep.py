import json
import json_utils
import json_file_operations
import json_validations
import os

schema_file = "test_run_store_schema.json"
tester_file = "test_run_store.dat"


def get_tester_data():

    if not os.path.isfile(tester_file):
        try:
            fobj = open(tester_file, 'w')
            fobj.write('{\"testerid\": "nnn\", \"testrunid\": \"1\"}')
            fobj.close()
        except:
            err_text = "Tester file does not exist and cannot create new file: " + tester_file
            json_utils.log_exceptions(err_text)
            raise ValueError()

    with open(tester_file) as fobj:
        try:
            tester_str = fobj.read()
            tester_dict = json.loads(tester_str)
            schema_in_json_dict = json_file_operations.get_json_from_json_file(schema_file)
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
            json_utils.log_exceptions(e)
            err_text = "Tester data file read or decoding failed: " + \
                       tester_file + " or " + schema_file
            json_utils.log_exceptions(err_text)
            raise ValueError()

        try:
            json_validations.validate_json_data(schema_in_json_dict, tester_dict)
        except ValueError as e:
            json_utils.log_exceptions(e)
            err_text = "Test data json validation failed: " + tester_file
            json_utils.log_exceptions(err_text)
            raise ValueError()

    with open(tester_file, 'w') as fobj:
        try:
            tester_dict["testrunid"] = str(int(tester_dict["testrunid"]) + 1)
            tester_str = json.dumps(tester_dict)
            fobj.write(tester_str)
        except FileNotFoundError as e:
            json_utils.log_exceptions(e)
            err_text = "Tester data file write failed: " + tester_file
            json_utils.log_exceptions(err_text)
            raise ValueError()

    return tester_dict
