import json
from jsonschema import exceptions, Draft7Validator
import json_utils


def validate_json_data(schema_in_dict, data_in_dict):
    try:
        Draft7Validator(schema_in_dict).validate(data_in_dict)
    except (exceptions.ValidationError, json.JSONDecodeError) as e:
        json_utils.log_exceptions(e)
        raise ValueError(e)
