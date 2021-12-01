import json
import urllib.request
import urllib.error

import json_utils


def get_json_from_url(url_address):
    url_data_dict = {}
    try:
        json_data = urllib.request.urlopen(url_address).read().decode()
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        json_utils.log_exceptions(e)
        err_text = "Request data from URL: " + url_address + " failed"
        json_utils.log_exceptions(err_text)
    else:
        try:
                url_data_dict = json.loads(json_data)
        except ValueError as e:
                json_utils.log_exceptions(e)
                err_text = "Parsing Json from URL failed"
                json_utils.log_exceptions(err_text)
    return url_data_dict

