import py_data.globvars as globvars

#  When updating testdata, please update the test set lists at the bottom of this module!

content = [
    {
        "testheader": {"testdescription": "My first poc scenario", "customer": globvars.poc_hit},
        "resources": [
            {"stocktype": "in",  "shelf_type": "yardAAA",      "net_value": "400000"},
            {"stocktype": "out", "shelf_type": "containerAAA", "net_value": "250000"}
        ]
    },
    {
        "testheader": {"testdescription": "My second poc scenario", "customer": "sämple"},
        "resources": [
            {"stocktype": "in",  "shelf_type": "yardAAA",      "net_value": "400004"},
            {"stocktype": "out", "shelf_type": "containerAAA", "net_value": "250001"}
        ]
    }
]
