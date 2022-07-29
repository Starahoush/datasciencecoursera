# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:41:07 2022

@author: Igor
"""

import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">+1 734 303 4456</phone>
    <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Name: ',tree.find('name').text)
print('Attr: ',tree.find('email').get('hide'))