# Small command line utility to print json in python
import json
import sys
import argparse
import pprint
import collections

import json_utils


def json_file_convert_to_python(file_name):
    with open(file_name) as fobj:
        try:
            tester_str = fobj.read()
            customdecoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
            customdecoder.decode(tester_str)
            print(tester_str)
        except (FileNotFoundError, ValueError) as e:
            json_utils.log_exceptions(e)
            err_text = "Json file not found or read file: " + file_name
            json_utils.log_exceptions(err_text)


def str_convert_to_python(json_string):
    try:
        tester_dict = json.loads(json_string)
        pprint.pprint(tester_dict, indent=4)
    except ValueError as e:
        json_utils.log_exceptions(e)
        err_text = "Json std input read failed"
        json_utils.log_exceptions(err_text)


def main(arguments):
    parser = argparse.ArgumentParser(usage="python util_json2python.py [ jsonfile -file_to_convert ]")
    parser.add_argument('--jsonfile', dest='json_file', help='Json file to be convertd to python')
    args = parser.parse_args()
    if args.json_file:
        file_to_conv = args.json_file
        json_file_convert_to_python(file_to_conv)
    else:
        json_string = sys.stdin.read()
        str_convert_to_python(json_string)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
