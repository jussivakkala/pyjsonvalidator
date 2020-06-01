import py_data.globvars as globvars


content = [
    {
        "testheader": {"testdescription": "My first scenario", "customer": "Aapeli"},
        "balances": [
            {"balanceid": "real", "bal_type": "money", "start": "500", "end": "499"},
            {"balanceid": "231", "bal_type": "receipt", "start": "250", "end": "250"},
        ],
        "services": [
            {"service_type": "1", "identifier": globvars.id_abel,  "price": "1.00000",
             "action": globvars.someconst, "someval": "", "subitems" : []
             },
            {"service_type": "2", "identifier": globvars.id_abel, "price": "0.00000",
             "action": globvars.someconst, "someval": "AAA111", "subitems" : [
                globvars.locitem,
                globvars.seclocitem
              ]
             }
        ]
    },
    {
        "testheader": {"testdescription": None, "customer": "Beepeli"},
        "balances": [
            {"balanceid": "real",  "bal_type": "money",  "start": "100",      "end": "499"},
            {"balanceid": "241",   "bal_type": "receipt",  "start": "200",     "end": "250"}
        ],
        "services": [
            {"service_type": "1", "identifier": globvars.id_abel,  "price": "1.00000",
             "action": globvars.someconst, "someval": "1", "subitems" : []
             }
        ]
    },
    {
        "testheader": {"testdescription": "My third scenario", "customer": "Ceepeli"},
        "balances": [
            {"balanceid": "real",  "bal_type": "money",  "start": "100",      "end": "499"},
            {"balanceid": "241",   "bal_type": "card",  "start": "200",     "end": "250"}
        ],
        "services": [
            {"service_type": "3", "identifier": globvars.id_abel,  "price": "1.00000",
             "action": globvars.someconst, "someval": "", "subitems" : []
             }
         ]
    }
]
