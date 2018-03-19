import boto3
import pandas as pd
from io import BytesIO
from sklearn.externals import joblib
from config import ACCESS_KEY_ID, SECRET_ACCESS_KEY

BUCKET_NAME = 'lca-model-bucket'
MODEL_FILE_NAME = 'rf_model.pkl'
MODEL_LOCAL_PATH = MODEL_FILE_NAME


def load_rf_model():
    client = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
    obj = client.get_object(Bucket=BUCKET_NAME, Key=MODEL_FILE_NAME)
    clf = joblib.load(BytesIO(obj['Body'].read()))
    return clf

def predict(data):
    clf = load_rf_model()
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