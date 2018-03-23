import pandas as pd
from sklearn.externals import joblib


def load_rf_model():
    """
        Function that reloads random forest object from pickle file.

        Args:

        Returns:
            clf (Random Forest Classifier): random forest object
        """
    clf = joblib.load('prediction/rf_model.pkl')
    return clf


def map_data_to_sample(data):
    """
        Function that maps user input data to pandas data frame.

        Args:
            data (dictionary): dictionary that contains user input for different attributes

        Returns:
            df (pandas.DataFrame object): data frame that holds test data
        """
    df = pd.DataFrame(
        [{
            'TOTAL_WORKERS': data['total_workers'],
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
    return df


def predict(data):
    """
        Function that returns predicted result given new test data.

        Args:
            data (dictionary): new test data

        Returns:
            result (integer): a binary response (0 or 1)
        """
    clf = load_rf_model()
    result = clf.predict(map_data_to_sample(data))
    result = result[0]  # get only the desired binary response
    return result

