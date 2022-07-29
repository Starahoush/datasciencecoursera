# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:41:07 2022

@author: Igor
"""

import json
data = '''
{
    "name": "Chuck",
    "phone": {
            "type": "intl",
            "number": "+1 734 303 4456"
    },
    "email": {
            "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name: ',info["name"])
print('Hide: ',info["email"]["hide"])