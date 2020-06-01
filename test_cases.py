import test_pre_proc

import py_data.locbulk
import py_data.locdata
import py_data.pocdata


regression_tests = [
    {'test_name': 'loc_pyth',    'testmodule': py_data.locdata.content,  'schemafile': './schemas/locschema.json',
                                                                         'prefunc': test_pre_proc.pre_loc},
    {'test_name': 'loc_json',    'testmodule': './py_data/locdata.json',           'schemafile': './schemas/locschema.json',
                                                                         'prefunc': test_pre_proc.pre_loc},
    {'test_name': 'loc_yaml',    'testmodule': './py_data/locdata.yaml',           'schemafile': './schemas/locschema.json',
                                                                         'prefunc': test_pre_proc.pre_loc},
    {'test_name': 'poc_test',    'testmodule': py_data.pocdata.content,  'schemafile': './schemas/pocschema.json',
                                                                         'prefunc': test_pre_proc.pre_poc},
    {'test_name': 'bulk_test',   'testmodule': py_data.locbulk.content,  'schemafile': './schemas/locschema.json',
                                                                         'prefunc': test_pre_proc.pre_bulk},
    {'test_name': 'loc_skipval', 'testmodule': py_data.locdata.content,  'schemafile':  None,
                                                                         'prefunc': None},
    {'test_name': 'btc_euro',    'testmodule': 'https://api.gdax.com/products/BTC-EUR/ticker',
                                 'schemafile': './schemas/btc_eur_schema.json', 'prefunc': None},
    {'test_name': 'city_nature', 'testmodule': 'https://citynature.eu/api/wp/v2/places?cityid=5',
                                 'schemafile': './schemas/city_nature_schema.json', 'prefunc': test_pre_proc.pre_city_nature},
]