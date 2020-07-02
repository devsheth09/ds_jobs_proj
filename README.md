# Salary Prediction Project

## Project Overview

* Created a tool that estimates salary for different Data Science roles to help with salary negotiation with future employer.

* Scrapped about 1000 job postings from glassdoor using python and selenium.

* Feature engineering done to quantify the postings which contained python, R, AWS, Spark, SQL, Tableau, Excel.

* Optimised Multiple Linear, Support Vector and Random Forest Regressors using RandomizedSearchCV.

* Built a client facing API using Flask.

## Resources

**Python Version** : 3.7.6

**Packages** :pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

**Web Framework Requirements** : pip install -r requirements.txt

**Project inspiration from Ken Jee's project walkthrough** : https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

**Scraper to scrap glassdoor job postings**: https://github.com/arapfaik/scraping-glassdoor-selenium

**Client API using Flask** : https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping for job postings from Glassdoor.com

Scraped 1000 job postings from glassdoor.com. Following fields were scraped from each posting :

 * Job title
 * Salary Estimate
 * Job Description
 * Rating
 * Company
 * Location
 * Company Headquarters
 * Company Size
 * Company Founded Date
 * Type of Ownership
 * Industry
 * Sector
 * Revenue
 * Competitors
 
## Data Preprocessing

* Parsed numeric data out of salary
* Parsed rating out of company text
* Made a new column for company state
* Made columns for employer provided salary and hourly wages
* Removed job postings without salary
* Added a column for if the job was at the company’s headquarters
* Transformed founded date into age of company
* Made columns for if different skills were listed in the job description:
   * Python
   * SQL
   * Tableau
   * R
   * Excel
   * AWS
   * Spark
* Column for simplified job title and Seniority
* Column for description length

