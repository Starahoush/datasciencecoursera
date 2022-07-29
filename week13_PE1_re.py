# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 10:00:06 2022

failed code; didnt lok for span tags (didnt read the asignment xD)

@author: Igor
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1460973.html').read()
soup = BeautifulSoup(html,'html.parser')

#tags = soup('a')
#for tag in tags:
#    print(tag.get('href', None))
text=soup.get_text()
ans = re.findall('[0-9]+',text)
sm = 0
for num in ans:
    sm += int(num)
print(ans)