#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:52:49 2020

@author: devanshsheth
"""
import pandas as pd
import numpy as np
import random
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score
from scipy.stats import uniform, truncnorm, randint
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVR

random.seed(123)
df = pd.read_csv('processed_data.csv')

df_input_columns=df[['Rating','Size','Type of ownership','Industry', 'Sector', 'Revenue','Hourly_salary',
                     'Employer_provided_salary', 'Avg_salary', 'State', 'Similar_state', 'Age',
                     'Python', 'R', 'SQL', 'Spark', 'AWS', 'Tableau', 'Excel', 'Categorized_title', 'Seniority',
                     'description_length', 'Number_of_Competitors']]

dummy_variables=pd.get_dummies(df_input_columns)

x = dummy_variables.drop('Avg_salary', axis =1)
y = dummy_variables.Avg_salary.values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)


# Multiple Linear regression
ml = LinearRegression()
ml.fit(x_train, y_train)
print(f'constant = {ml.intercept_}')
print(f'coefficients = {ml.coef_}')
prediction_ml=ml.predict(x_test)
print('Prediction of multiple linear regression>', prediction_ml )

# #Support Vector Regression
sv = SVR(kernel='poly', C=1e2, degree=3)
pred=sv.fit(x_train, y_train)
prediction_svr=pred.predict(x_test)
print('Prediction of support vector regression>', prediction_svr )


#Random forest regression
rf = RandomForestRegressor()
model_params = {
    'n_estimators': randint(4,200),
    'max_features': truncnorm(a=0, b=1, loc=0.25, scale=0.1),
    'min_samples_split': uniform(0.01, 0.199)
}

#Tuning the random forest regression with RandomizedSearchCV

clf = RandomizedSearchCV(rf, model_params, n_iter=100, cv=5, random_state=1)
model = clf.fit(x_train, y_train)
tpred_rf = model.best_estimator_.predict(x_test)


#Model Evaluation

#multiple linear regression evaluation
cross_val_score_ml =np.mean(cross_val_score(ml,x_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))
print('MAE for multiple linear regression >',mean_absolute_error(y_test,prediction_ml))

#Support vector regression
cross_val_score_svr=np.mean(cross_val_score(pred,x_train,y_train,scoring = 'neg_mean_absolute_error', cv= 4))
print('MAE for support vector regression >',mean_absolute_error(y_test,prediction_svr))

#Random forest regression
cross_val_score_rf=np.mean(cross_val_score(rf,x_train,y_train,scoring = 'neg_mean_absolute_error', cv= 4))
print('MAE for random forest regression >',mean_absolute_error(y_test,tpred_rf))


pickl = {'model': model.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
    