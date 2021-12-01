import json
from jsonschema import exceptions
import validators

import json_utils
import json_file_operations
import json_web_operations
import json_validations



def validate_and_set_input_file(test_dict):
    try:
        test_dict['testmodule']
    except KeyError:
        json_utils.log_exceptions('test data key \"{}\" not found'.format(test_dict))
        raise ValueError

    file_extensions = ('.json', '.yaml')

    input_file = test_dict['testmodule']

    # Match Python dictionary in memory
    if type(input_file) is not str:    # data is python variable
        return test_dict['testmodule']

    # Match URL
    valid = validators.url(test_dict['testmodule'])
    if valid:
        test_run = json_web_operations.get_json_from_url(test_dict['testmodule'])
        return test_run

    input_file_ext = input_file[-5:]

    if json_utils.is_string_valid(input_file) is False or input_file_ext not in file_extensions:
        json_utils.log_exceptions('Invalid or unknown file type: ' + input_file)
        raise ValueError

    try:
        # Match JSON in file
        if '.json'.__eq__(input_file_ext):
            test_run = json_file_operations.get_json_from_json_file(input_file)
            return test_run
        # Match YAML in file
        elif '.yaml'.__eq__(input_file_ext):
            test_run = json_file_operations.get_yaml_from_yaml_file(input_file)
            return test_run
        else:
            json_utils.log_exceptions('Unknown file type: ' + input_file)
            raise ValueError
    except (FileNotFoundError):
        json_utils.log_exceptions('Cannot open test data file: ' +
                                  test_dict['testmodule'])
        raise FileNotFoundError
    except (ValueError):
        json_utils.log_exceptions('Cannot validate test data file: ' +
                                  test_dict['testmodule'])
        raise ValueError
    except:
        raise


def json_validation(test_dict, modifications_in, replace_file=None):
    try:
        test_run = validate_and_set_input_file(test_dict)
    except (ValueError, FileNotFoundError) as e:
        json_utils.log_exceptions('Json validation failed')
        raise ValueError(e)

    validate_schema = False
    if json_utils.is_string_valid(test_dict['schemafile']):
        schema_file = test_dict['schemafile']
        validate_schema = True

    call_preproc = False
    if test_dict['prefunc'] is not None:
        modification_func = test_dict['prefunc']
        call_preproc = True

    if validate_schema:
        schema_in_json_dict = json_file_operations.get_json_from_json_file(schema_file)

    try:
        if call_preproc:
            # Do all table specific data modifications here
            item = modification_func(test_run, modifications_in)
        else:
            item = test_run

        item_in_str = json.dumps(item)
        item_in_json = json.loads(item_in_str)
        if validate_schema:
                 json_validations.validate_json_data(schema_in_json_dict, item_in_json)
    except exceptions.ValidationError as e:
        error_message = \
            '\n++++++++++++ Json validation failed +++++++++++'
        json_utils.log_exceptions(e)
        json_utils.log_exceptions(error_message)
        raise ValueError(e)

    return item
