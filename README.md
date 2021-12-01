# Json modification and validation routines for Python

Import, modify and validate from/to data in json, yaml and python format.
A few utilities and usage examples are demonstrated.

Original business need has been evolved from need to handle complex data structures for automated test cases, often 
with several nesting dictionaries and lists of data required for test preparation, test execution and verifying expected test results. 
Those could be for example per testcase:
customer data preparation, serie of transactions executed and expected test result verification.
That said, there could be also many other business cases for these routines!

Further there has been need to modify static test data on the fly with tester specific, time dependent etc. attributes.
The aim has been to isolate the test data and test data validation rules from the code logic as much as possible.
This project source code provides an easy basis for further development.

## Getting started by running some of the examples

- check that Python 3.* has been installed
- check that jsonschema and yaml python libraries are installed (read 'Prerequisites' below) 
- go to the directory where you copied the project
- run from the command line the default example: 'python cmd_json_test.py'
- if you have Robot Framework installed, you can run an example in command line: 'robot .'
- verify output on console and created files
- add more schemas and data processing to suit your own needs!

## Introduction to features

- Json or yaml file and python dictionary -format input option for data validation  and modification  
- Importing of larger lists with 1000's of items (where each item in array is validated against one schema file) is demonstrated  
- Input data premodification (before schema validation) with function pointers (datetime.now etc.) is demonstrated  
- Input data premodification (before schema validation) from file  (tester id, test run id etc) feature demonstrated  
- Example preprocessing configuration record (currently in test_cases.py module) each row for one data type:  
regression_tests = [  
     {'test_name': 'loc_pyth',    'testmodule': py_data.locdata.content,  'schemafile': './schemas/locschema.json', 'prefunc': test_pre_proc.pre_loc},
                                                                         
    {'test_name': 'loc_json',    'testmodule': './py_data/locdata.json', 'schemafile': './schemas/locschema.json', 'prefunc': test_pre_proc.pre_loc},
    
    {'test_name': 'loc_yaml',    'testmodule': './py_data/locdata.yaml', 'schemafile': './schemas/locschema.json', 'prefunc': test_pre_proc.pre_loc},
    
    {'test_name': 'poc_test',    'testmodule': py_data.pocdata.content,  'schemafile': './schemas/pocschema.json', 'prefunc': test_pre_proc.pre_poc},
    
    {'test_name': 'loc_skipval', 'testmodule': py_data.locdata.content,  'schemafile':  None, 'prefunc': None},
     
    {'test_name': 'btc_euro',    'testmodule': 'https://api.gdax.com/products/BTC-EUR/ticker', 'schemafile': './schemas/btc_eur_schema.json', 'prefunc': None},
    
    {'test_name': 'city_nature', 'testmodule': 'https://citynature.eu/api/wp/v2/places?cityid=5', 'schemafile': None, 'prefunc': None},
]  
    * ... where 'testmodule': '<somefile>.json' indicates json data input. 
    * ... where 'testmodule': '<somefile>.yaml' indicates yaml data input  
	* ... where 'testmodule': <somevar> (note: without quotes) indicates python data input from variable (typically from imported variable file)  
	please note that file with referred variable *must* exist at runtime.
    * ... where 'testmodule': '<some_valid_json_url>' indicates external web source for data input 
	
    * ... where 'prefunc' is a function pointer variable to do all preprocessing for input data     
      * examples of preprocessing functions are shown in test_pre_proc.py module
    * ... if you want to skip json schema validation:  'schemafile': None
    * ... if you want to skip preprocessing function call: 'prefunc': None 
  
- complex json schema validation examples with nested lists, dictionaries and validation keywords are demonstrated
    -> enum list
    -> allow null value
    -> length
    -> value range, digit, alpha, alphadigit etc..
    -> common format, date, time, etc.
    -> regex

- python output for json input data file utility (without schema validation, check util_json2python.py in project)

- Robot Framework suite to consume validated data is demonstrated

## Modules

#### Input data
./py_data

#### Data validation schemas
./schemas  

#### Business logic dependent modules
test_cases.py
test_pre_proc.py
test_run_data.py
test_run_store.dat
test_run_store_schema.json
test_validations.py

#### Core functionality:
json_file_operations.py
json_utils.py
json_validations.py
json_web_operations.py

#### Caller module examples
cmd_json_test.py

#### Separate command line utilities
util_json2python.py

#### Unit tests
unit_test_validations.py

#### Unit test data
./unit_test/

#### Robot Framework call example
test_json.robot

#### Required libraries and tools
jsonschema, validators and pyyaml are installed (command line 'pip install <library>' suffices, if you have pip installed)  
Current versions of needed libraries (listed with pipreqs -tool)  
jsonschema==3.0.1  
validators==0.15.0  
pyyaml==5.3.1  
(optional) robotframework==3.1.1

## Prerequisites

python 3.* installed  

## Running the unit test

'python -m unit_test_validations'

## Authors

* Jussi Vakkala 


