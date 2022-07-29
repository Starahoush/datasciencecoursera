# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:56:41 2022

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

@author: Igor
"""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

xml = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1460975.xml').read()
tree = ET.fromstring(xml)

counts = tree.findall('.//count')

print(sum([int(res.text) for res in counts]))
#print('Name: ',counts.find('count').text)
#print('Attr: ',counts.find('name'))