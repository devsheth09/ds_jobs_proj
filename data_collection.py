#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:54:04 2020

@author: devanshsheth
"""

import glassdoorScraper as sc
import pandas as pd

df = sc.get_jobs('data scientist', 10, False, 12)

df.to_csv('scrapped_jobs.csv', index = False)
