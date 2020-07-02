#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 00:15:43 2020

@author: devanshsheth
"""

import requests
from data_for_api import Api_data

URL = 'http://127.0.0.1:5000/predict'

headers = {"Content-Type": "application/json"}
data = {"input": Api_data}

r = requests.get(URL,headers=headers, json=data)

r.json()