# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:07:35 2022

@author: Igor
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))