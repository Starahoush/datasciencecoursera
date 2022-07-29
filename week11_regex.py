# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:24:48 2022

^ Matches the beginning of a line

$ Matches the end of the line

. Matches any character

\s Matches whitespace

\S Matches any non-whitespace character

* Repeats a character zero or more times

*? Repeats a character zero or more times (non-greedy)

+ Repeats a character one or more times

+? Repeats a character one or more times (non-greedy)

[aeiou] Matches a single character in the listed set

[^XYZ] Matches a single character not in the listed set

[a-z0-9] The set of characters can include a range

( Indicates where string extraction is to start

) Indicates where string extraction is to end

@author: Igor
"""

import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

re.findall('\S+@\S+?',x) #returns only ['stephen.marquard@u']

re.findall('\S+?@\S+',x) #but this returns ['stephen.marquard@uct.ac.za']

#( ) are very powerful since we can use a bigger matching but demand the extraction of a given part

re.findall('\S+?@(\S+)',x) #will return only everything after the @ ['uct.ac.za']

#another example

re.findall('^From (\S+?@\S+)',x) #will return only the email but match the '^From ' ['stephen.marquard@uct.ac.za']

re.findall('@([^ ]*)', x) #['uct.ac.za']