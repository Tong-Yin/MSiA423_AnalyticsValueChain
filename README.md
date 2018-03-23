# LCA Case Status Prediction Project

## Project Team
* Developer: Tong Yin
* Product Owner: Joe Gilbert
* QA: Grace Cui

## Project Objective
This repo can be used to reproduce a Labor Condition Application (LCA) case status prediction web app. The app is written with `Python 3` and is currently running at http://lca-app-env.7du6j6wmpd.us-east-2.elasticbeanstalk.com.

## Project Charter

* Vision: Help employers forecast their petition result and understand the process of getting their LCA approved
* Mission: Predict the LCA case status using data from employer’s LCA and the case certification determinations processed by OFLC
* Success Criteria: A web app that returns Yes for Certified and No for Denied after user inputs a set of attributes.

## Data
Raw data can be accessed through https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Disclosure_Data_FY17.xlsx. Helper functions to do EDA and data cleaning can be found at `data/data_process_helper.py`. You need to run the script at `data/make_dataframe.py` to generate a cleaned data frame.

## Pivotal Tracker
[Link to Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2143075)

## Prerequisites
Things you need to get it started:
* AWS account
* [conda](https://anaconda.org/): Either Anaconda or Miniconda is fine for this project.
* [git](https://git-scm.com/): You will most likely need version control.

## Steps to deploy app using AWS Elastic Beanstalk
Below is a tutorial for setting up the app on AWS. For general guidance on Flask app deployment on AWS, 
you can refer to [this tuturial](https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80)

1. Clone this GitHub repo to a local directory. 

2. Create a project environment

If using Anaconda, create conda environment by:

`conda env create -f lca_env.yml`

If using Python virtualenv (suggested version `Python 3.5`), create Python virtualenv and install required packages by:

`pip install -r requirements.txt`

3. In the same directory as `requirements.txt`, create a configuration file called `config.py` to configure your RDS connection.

`SECRET_KEY = 'secret_key'`

`SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<db_user>:<db_password>@<endpoint>/<db_url>'`

`SQLALCHEMY_TRACK_MODIFICATIONS = True`

`ACCESS_KEY_ID = 'your_access_key_id'`

`SECRET_ACCESS_KEY = 'your_secret_access_key`

4. To initialize a database on RDS, please run `create_initial_db.py` under `database` folder.

5. Now run `application.py`. The app should be running on your local environment. Any info you enter will be saved to your RDS database.

6. To deploy the app using Elastic Beanstalk, please run the following commands and follow Elastic Beanstalk prompts:

`pip install eb`

`eb init`

`eb create`

7. To update deployed app, run the following command: 

`eb deploy` 

## Logging


## Unit Testing
