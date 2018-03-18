import pandas as pd
import pickle
from flask import url_for
import os


def predict(data):
    path = './clf.pkl'
    if not os.path.exists(path):
        path = 'src/clf.pkl'
    fileObject = open(path, 'rb')
    clf = pickle.load(fileObject)
    fileObject.close()
    result = clf.predict(map_data_to_sample(data))
    return result[0]


def map_data_to_sample(data):
    return pd.DataFrame(
        [{'TOTAL_WORKERS': data['total_workers'],
           'NEW_EMPLOYMENT': data['new_employment'],
           'CONTINUED_EMPLOYMENT': data['continued_employment'],
           'CHANGE_PREVIOUS_EMPLOYMENT': data['change_previous_employment'],
           'NEW_CONCURRENT_EMPLOYMENT': data['new_concurrent_employment'],
           'CHANGE_EMPLOYER': data['change_employer'],
           'AMENDED_PETITION': data['amended_petition'],
           'FULL_TIME_POSITION_CODE': data['full_time_position_code'],
           'H1B_DEPENDENT_CODE': data['h1b_dependent_code'],
           'WILLFUL_VIOLATOR_CODE': data['willful_violator_code'],
           'WAGE_UNIT_OF_PAY': data['wage_unit_of_pay'],
           'PREVAILING_WAGE': data['prevailing_wage'],
           'WAGE_RATE_OF_PAY_FROM': data['wage_rate_of_pay_from'],
           'WAGE_RATE_OF_PAY_TO': data['wage_rate_of_pay_to']
           }
        ]
    )