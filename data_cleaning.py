#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:41:40 2020

@author: devanshsheth
"""

import pandas as pd

df= pd.read_csv('scrapped_jobs.csv')
print(df)

df = df.drop(['Unnamed: 0'], axis =1)

# To remove Nan values from the salary estimate column before splitting the column as it is not possible to perform splitting if the column contains Nan values

df['Hourly_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Employer_provided_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)


df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
remove_k_from_salary = salary.apply(lambda x : x.replace('K' ,'').replace('$' ,''))

hr= remove_k_from_salary.apply(lambda x: x.lower().replace('per hour' ,'').replace('employer provided salary:' ,''))

df['Min_salary' ]= hr.apply(lambda x : int(x.split('-')[0]))
df['Max_salary' ]= hr.apply(lambda x : int(x.split('-')[1]))
df['Avg_salary'] = (df['Min_salary' ] +df['Max_salary']).div(2)

df['Company' ]= df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)
df['State'] = df['Location'].apply(lambda x: x.split(',')[1])

# Replacing Los Angeles
df['State'] = df.State.apply(lambda x: x.strip() if x.strip().lower() != 'los angeles' else 'CA')
df['Similar_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
df['Age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R'] = df['Job Description'].apply(lambda x: 1 if 'rstudio' in x.lower() or 'r-studio' in x.lower() else 0)
df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['Tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.to_csv('Cleaned_data.csv', index = False)
