"""
This module includes unit tests for two important functions in data_process_helper.py.
"""

import pandas as pd
import numpy as np
from data import data_process_helper as helper


def test_impute_missing_cat():
    """Testing impute_missing_cat function."""

    # data frame inputs
    df_inputs = {
        "AGENT_REPRESENTING_EMPLOYER": [np.nan, 'Y', 'N', 'N', 'Y', np.nan, np.nan],
        "H1B_DEPENDENT": [np.nan, 'Y', 'N', np.nan, 'N', 'N', np.nan],
        "WILLFUL_VIOLATOR": [np.nan, 'Y', 'N', np.nan, 'N', 'N', np.nan]
    }
    df_testing = pd.DataFrame(data=df_inputs)

    # actual output
    actual = helper.impute_missing_cat(df_testing)

    # expected output
    df_expected = {
        "AGENT_REPRESENTING_EMPLOYER": ['Y', 'Y', 'N', 'N', 'Y', 'Y', 'Y'],
        "H1B_DEPENDENT": ['N', 'Y', 'N', 'N', 'N', 'N', 'N'],
        "WILLFUL_VIOLATOR": ['N', 'Y', 'N', 'N', 'N', 'N', 'N']
    }
    expected = pd.DataFrame(data=df_expected)

    try:
        # check type
        assert isinstance(expected, pd.DataFrame)

        # check expected output
        assert actual.equals(expected)
        print('Test for impute_missing_cat function PASSED!')
    except:
        print('Test for impute_missing_cat function FAILED!')


def test_add_binary():
    """Testing add_binary function."""

    # data frame inputs
    df_inputs = {
        'CASE_STATUS': ['CERTIFIED', 'CERTIFIED', 'CERTIFIED-WITHDRAWN', 'DENIED', 'DENIED', 'CERTIFIED'],
        'FULL_TIME_POSITION': ['Y', 'Y', 'N', 'N', 'N', 'N'],
        'H1B_DEPENDENT': ['Y', 'Y', 'N', 'N', 'N', 'N'],
        'WILLFUL_VIOLATOR': ['Y', 'Y', 'N', 'N', 'N', 'N']
    }
    df_testing = pd.DataFrame(data=df_inputs)
    for col in ['CASE_STATUS', 'FULL_TIME_POSITION', 'H1B_DEPENDENT', 'WILLFUL_VIOLATOR']:
        df_testing[col] = df_testing[col].astype('category')

    # actual output
    actual = helper.add_binary(df_testing)

    # expected output
    df_expected = {
        'CASE_STATUS': ['CERTIFIED', 'CERTIFIED', 'CERTIFIED-WITHDRAWN', 'DENIED', 'DENIED', 'CERTIFIED'],
        'FULL_TIME_POSITION': ['Y', 'Y', 'N', 'N', 'N', 'N'],
        'H1B_DEPENDENT': ['Y', 'Y', 'N', 'N', 'N', 'N'],
        'WILLFUL_VIOLATOR': ['Y', 'Y', 'N', 'N', 'N', 'N'],
        'FULL_TIME_POSITION_CODE': [1, 1, 0, 0, 0, 0],
        'H1B_DEPENDENT_CODE': [1, 1, 0, 0, 0, 0],
        'WILLFUL_VIOLATOR_CODE': [1, 1, 0, 0, 0, 0],
        'CASE_STATUS_CODE': [1, 1, 0, 0, 0, 1]
    }
    expected = pd.DataFrame(data=df_expected)
    expected = expected[['CASE_STATUS',
                         'FULL_TIME_POSITION',
                         'H1B_DEPENDENT',
                         'WILLFUL_VIOLATOR',
                         'FULL_TIME_POSITION_CODE',
                         'H1B_DEPENDENT_CODE',
                         'WILLFUL_VIOLATOR_CODE',
                         'CASE_STATUS_CODE']]
    for col in ['CASE_STATUS', 'FULL_TIME_POSITION', 'H1B_DEPENDENT', 'WILLFUL_VIOLATOR']:
        expected[col] = expected[col].astype('bool')

    try:
        # check type
        assert isinstance(expected, pd.DataFrame)

        # check expected output
        assert actual.equals(expected)
        print('Test for add_binary function PASSED!')
    except:
        print('Test for add_binary function FAILED!')


def main():
    """Main function"""

    test_impute_missing_cat()
    test_add_binary()


if __name__ == "__main__":
    main()