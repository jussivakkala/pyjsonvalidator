import json
import json_utils
import yaml


def get_json_from_json_file(file_name):
    try:
        with open(file_name) as fobj:
            try:
                schema_in_json_str = fobj.read()
                schema_in_json_dict = json.loads(schema_in_json_str)
            except (TypeError, json.JSONDecodeError) as e:
                json_utils.log_exceptions("Json decoding failed on : " + file_name)
                json_utils.log_exceptions(e)
                raise ValueError
    except FileNotFoundError as e:
        json_utils.log_exceptions(e)
        print("Json schema file read failed on: " + file_name)
        raise FileNotFoundError

    return schema_in_json_dict


def write_python_to_json_file(file_name, python_dict):
    with open(file_name, 'w', encoding='utf8') as fobj:
        try:
            json_string = json.dumps(python_dict, sort_keys=False, indent=4, ensure_ascii=False)
            fobj.write(json_string)
        except FileNotFoundError as e:
            json_utils.log_exceptions(e)
            err_text = "Json file write failed: " + file_name
            json_utils.log_exceptions(err_text)
            raise ValueError()


def get_yaml_from_yaml_file(file_name):
    try:
        with open(file_name) as fobj:
            try:
                yaml_in_str = yaml.safe_load(fobj.read())
                json_in_str = json.dumps(yaml_in_str)
                data_in_json_dict = json.loads(json_in_str)
            except (TypeError, json.JSONDecodeError, yaml.YAMLError) as e:
                json_utils.log_exceptions("Yaml data conversion failed on : " + file_name)
                json_utils.log_exceptions(e)
                raise ValueError
    except FileNotFoundError as e:
        json_utils.log_exceptions(e)
        print("Yaml data read failed on: " + file_name)
        raise FileNotFoundError

    return data_in_json_dict


def write_python_to_yaml_file(file_name, python_dict):
    with open(file_name, 'w', encoding='utf8') as fobj:
        try:
            yaml.dump(python_dict, fobj, default_flow_style=False, sort_keys=False, indent=4, allow_unicode=True)
        except FileNotFoundError as e:
            json_utils.log_exceptions(e)
            err_text = "Yaml file write failed: " + file_name
            json_utils.log_exceptions(err_text)
            raise ValueError()

