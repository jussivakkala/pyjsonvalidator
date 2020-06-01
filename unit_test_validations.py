import unittest

import test_validations
import json_file_operations
from jsonschema import exceptions

import test_pre_proc

import unit_test.unit_test_data as unit_test_data
import unit_test.unit_test_bulk as unit_test_bulk
import unit_test.unit_test_data_invalid as unit_test_invalid


unit_test_details = [
    {'test_name': 'unit_test_pyth', 'testmodule': unit_test_data.content,
     'schemafile':'./unit_test/test_schema.json', 'prefunc': test_pre_proc.pre_test},
    {'test_name': 'unit_test_bulk', 'testmodule': unit_test_bulk.content,
     'schemafile':'./unit_test/test_schema.json', 'prefunc': test_pre_proc.pre_test},
    {'test_name': 'unit_test_json', 'testmodule': './unit_test/unit_test_data.json',
     'schemafile':'./unit_test/test_schema.json', 'prefunc': test_pre_proc.pre_test},
    {'test_name': 'unit_test_yaml', 'testmodule': './unit_test/unit_test_data.yaml',
     'schemafile':'./unit_test/test_schema.json', 'prefunc': test_pre_proc.pre_test},
    {'test_name': 'unit_test_no_schema', 'testmodule': './unit_test/unit_test_data.yaml',
     'schemafile': None,  'prefunc': test_pre_proc.pre_test},
    {'test_name': 'unit_test_no_prefunc', 'testmodule': './unit_test/unit_test_data.json',
     'schemafile': None, 'prefunc': None},
    {'test_name': 'unit_test_no_prefunc', 'testmodule': './unit_test/file_not_exists.json',
     'schemafile': None, 'prefunc': None},
    {'test_name': 'unit_test_no_prefunc', 'testmodule': './unit_test/unit_test_data.json',
     'schemafile': 'not_found_schema.json', 'prefunc': None},
    {'test_name': 'unit_test_no_prefunc', 'testmodule': './unit_test/unit_test_data.json',
     'schemafile': None, 'prefunc': 'my_str_function'},
    {'test_name': 'unit_test_pyth', 'testmodule': unit_test_invalid.content,
     'schemafile': './unit_test/test_schema.json', 'prefunc': test_pre_proc.pre_test},
]


class TestPyGen(unittest.TestCase):

    def test_schema_file_validation(self):
        schema_in_json_dict = json_file_operations.get_json_from_json_file('./unit_test/test_schema.json')
        self.assertEqual(schema_in_json_dict['items']['properties']['testheader']['properties']['test_run_id']['pattern'],
                         '^[0-9]+$', 'Schema file: validation failed')
        self.assertRaises(FileNotFoundError, json_file_operations.get_json_from_json_file, 'not_exist_file.json')
        self.assertRaises((exceptions.SchemaError, ValueError), json_file_operations.get_json_from_json_file,
                          './unit_test/test_invalid_schema.json')


    def test_success_test_item(self):
        # python data
        test_run = test_validations.json_validation(unit_test_details[0], {'change_to': 'TARG_PAT'})
        self.assertRegex(test_run[0]['testheader']['test_run_id'], '^[0-9]{1,12}$', 'Incorrect testrunid')
        self.assertEqual(test_run[0]['services'][1]['someval'], 'TARG_PAT111', 'Online changed pattern failed')
        self.assertEqual(test_run[1]['testheader']['testdescription'], None, 'testdescription header failed')
        self.assertEqual(test_run[1]['balances'][1]['balanceid'], '241', 'balanceid failed')
        self.assertEqual(test_run[1]['services'][0]['price'], '1.00000', 'price failed')
        self.assertEqual(len(test_run[1]['services']), 1, 'Array lenght mismatch with input data')
        # json data
        test_run = test_validations.json_validation(unit_test_details[2], {'change_to': 'TARG_PAT'})
        self.assertRegex(test_run[0]['testheader']['test_run_id'], '^[0-9]{1,12}$', 'Incorrect testrunid')
        self.assertEqual(test_run[0]['services'][1]['someval'], 'TARG_PAT111', 'Online changed pattern failed')
        self.assertEqual(test_run[1]['services'][0]['price'], '1.00000', 'price failed')
        # yaml data
        test_run = test_validations.json_validation(unit_test_details[3], {'change_to': 'TARG_PAT'})
        self.assertRegex(test_run[0]['testheader']['test_run_id'], '^[0-9]{1,12}$', 'Incorrect testrunid')
        self.assertEqual(test_run[0]['services'][1]['someval'], 'TARG_PAT111', 'Online changed pattern failed')
        self.assertEqual(test_run[1]['services'][0]['price'], '1.00000', 'price failed')

        # yaml data, no schema file
        test_run = test_validations.json_validation(unit_test_details[4], {'change_to': 'TARG_PAT'})
        self.assertRegex(test_run[0]['testheader']['test_run_id'], '^[0-9]{1,12}$', 'Incorrect testrunid')
        self.assertEqual(test_run[0]['services'][1]['someval'], 'TARG_PAT111', 'Online changed pattern failed')
        self.assertEqual(test_run[1]['services'][0]['price'], '1.00000', 'price failed')
        # no pre-modification function, no schema file
        test_run = test_validations.json_validation(unit_test_details[5], {'change_to': 'TARG_PAT'})
        self.assertEqual(test_run[1]['services'][0]['price'], '1.00000', 'price failed')


    def test_failed_test_item(self):
        # testmodule does not exist
        self.assertRaises(ValueError, test_validations.json_validation, unit_test_details[6],
                          {'change_to': 'pat_to'})
        # schmafile does not exist
        self.assertRaises(FileNotFoundError, test_validations.json_validation, unit_test_details[7],
                          {'change_to': 'pat_to'})
        # prefunc of wrong data type
        self.assertRaises(TypeError, test_validations.json_validation, unit_test_details[8],
                          {'change_to': 'pat_to'})
        # schema validation error
        self.assertRaises(ValueError, test_validations.json_validation, unit_test_details[9],
                          {'change_to': 'pat_to'})


if __name__ == '__main__':
    unittest.main(buffer=True)