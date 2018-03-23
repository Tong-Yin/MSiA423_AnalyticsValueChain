import pandas as pd
from sklearn.utils import resample
import numpy as np


def drop_false_predictor(df):
    """
    Function that drops false predictors.

    This function drops attributes with unique values such as Case_Number,
    Employer_Address, Employer_Phone and Employer_Phone_Ext, Agent_Attorney_Name,
    which are are unnecessary attributes in predicting the Case_Status.
    This is because attributes with unique values such as ID can build a model
    that would be based on that attribute with unique value and predict with maximum accuracy.

    Args:
        df (pandas.DataFrame object): data frame that holds all data

    Returns:
        df (pandas.DataFrame object): data frame with false predictors removed
    """
    df = df.drop(columns=['CASE_NUMBER', 'EMPLOYER_ADDRESS',
                          'EMPLOYER_PHONE', 'EMPLOYER_PHONE_EXT', 'AGENT_ATTORNEY_NAME'])
    return df


def drop_repetitive_predictors(df):
    """
    Function that drops repetitive predictors.

    This function drops attributes providing redundant information.
    Employer_City, Worksite_City, Worksite_County, Employer_Province, Employer_Postal_Code,
    Job_Title, SOC_Code, PW_Unit_Of_Pay, and PW_Wage_Level will be removed.
    Employer_State, Worksite_State, SOC_Name and WAGE_UNIT_OF_PAY will be kept.

    Args:
        df (pandas.DataFrame object): data frame with false predictors removed

    Returns:
        df (pandas.DataFrame object): data frame with repetitive predictors further removed
    """
    df = df.drop(columns=['EMPLOYER_CITY', 'EMPLOYER_COUNTRY', 'WORKSITE_CITY', 'WORKSITE_COUNTY',
                          'EMPLOYER_PROVINCE', 'EMPLOYER_POSTAL_CODE', 'WORKSITE_POSTAL_CODE',
                          'JOB_TITLE', 'SOC_CODE', 'PW_UNIT_OF_PAY', 'PW_WAGE_LEVEL'])
    return df


def drop_sparse_predictors(df):
    """
    Function that drops attributes with more than 50% missing values where there is no imputation possibility.

    This function drops attributes that include more than 50% missing values.
    These attributes are Agent_Attorney_City, Agent_Attorney_State, Original_Cert_Date,
    Employer_Business_DBA, Support_H1B, Labor_Con_Agree, Public_Disclosure_Location.

    Args:
        df (pandas.DataFrame object): data frame with false and repetitive predictors removed

    Returns:
        df (pandas.DataFrame object): data frame with predictors containing
        more than 50% missing values further removed
    """
    df = df.drop(columns=['AGENT_ATTORNEY_CITY', 'AGENT_ATTORNEY_STATE', 'ORIGINAL_CERT_DATE',
                      'EMPLOYER_BUSINESS_DBA', 'SUPPORT_H1B',
                      'LABOR_CON_AGREE', 'PUBLIC_DISCLOSURE_LOCATION'])
    return df


def drop_irrelevant_predictors(df):
    """
    Function that drops other attributes irrelevant for predictive model development.

    This function drops attributes that are not likely to be available to web app users
    (Case_Submitted, Decision_Date, NAICS_Code, PW_Source_Other, PW_Source_Year),
    and attributes not in compliance with regulations after data exploration
    (Employment_Start_Date, Employment_End_Date, since employment time cannot be more than three years
    while more than 90% have a difference more than 3 years for our dataset)

    Args:
        df (pandas.DataFrame object): data frame with false, repetitive, and sparse predictors removed

    Returns:
        df (pandas.DataFrame object): data frame with other irrelevant predictors further removed
    """
    df = df.drop(columns=['EMPLOYMENT_START_DATE','EMPLOYMENT_END_DATE',
                          'NAICS_CODE', 'PW_SOURCE_OTHER', 'PW_SOURCE_YEAR',
                          'CASE_SUBMITTED', 'DECISION_DATE'])
    return df


def convert_types(df):
    """
    Function that converts attribute types.

    This function converts certain attributes to actionable or correct types that can be used
    in future model development.

    Args:
        df (pandas.DataFrame object): data frame with all irrelevant predictors removed

    Returns:
        df (pandas.DataFrame object): data frame with converted predictors
    """
    # the following attributes have multiple levels
    list_cat = ['VISA_CLASS','WAGE_UNIT_OF_PAY','PW_SOURCE',
                'CASE_STATUS','SOC_NAME',
                'EMPLOYER_STATE','WORKSITE_STATE','FULL_TIME_POSITION',
                'H1B_DEPENDENT','WILLFUL_VIOLATOR','AGENT_REPRESENTING_EMPLOYER']
    for i in list_cat:
        df[i] = df[i].astype('category')

    # the following attributes have values equal to or larger than 0
    # most equal to 0 or 1 while a small portion larger than 1
    # treat those data points larger than 0 as 1 and those equal to 0 as 0
    # to simplify prediction and remove outliers
    # may be better without these; have to train model first and retrain?
    list_bool = ['NEW_EMPLOYMENT','CONTINUED_EMPLOYMENT','CHANGE_PREVIOUS_EMPLOYMENT',
                 'NEW_CONCURRENT_EMPLOYMENT','CHANGE_EMPLOYER','AMENDED_PETITION']
    for j in list_bool:
        df[j] = df[j].astype('bool')

    return df


def impute_missing_cat(df):
    """
    Function that imputes missing values.

    This function imputes certain categorical attributes with missing values
    using the most common type method. After imputation, the function also removes
    the very small portion of observations with missing values.

    Args:
        df (pandas.DataFrame object): data frame before imputation of missing values

    Returns:
        df (pandas.DataFrame object): data frame with no missing values left
    """
    df = df.fillna({"AGENT_REPRESENTING_EMPLOYER": "Y"})
    df = df.fillna({"H1B_DEPENDENT": "N"})
    df = df.fillna({"WILLFUL_VIOLATOR": "N"})
    df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    return df


def add_binary(df):
    """
    Function that converts certain multi-level categorical attributes to binary indicators

    Args:
        df (pandas.DataFrame object): data frame

    Returns:
        df (pandas.DataFrame object): data frame that contains created binary indicators
    """
    list = ['CASE_STATUS','FULL_TIME_POSITION','H1B_DEPENDENT','WILLFUL_VIOLATOR']
    want_binary = df[list].copy()
    df["FULL_TIME_POSITION_CODE"] = np.where(want_binary["FULL_TIME_POSITION"].str.contains("Y"), 1, 0)
    df["H1B_DEPENDENT_CODE"] = np.where(want_binary["H1B_DEPENDENT"].str.contains("Y"), 1, 0)
    df["WILLFUL_VIOLATOR_CODE"] = np.where(want_binary["WILLFUL_VIOLATOR"].str.contains("Y"), 1, 0)
    df["CASE_STATUS_CODE"] = want_binary["CASE_STATUS"].cat.codes
    df["CASE_STATUS_CODE"] = np.where(df["CASE_STATUS_CODE"] == 0, 1, 0)
    for l in list:
        df[l] = df[l].astype('bool')
    return df


def additional_processing(df):
    """
    Function that filters only the information we want and
    removes irrelevant attributes or observations after further EDA
    and factorizes certain attributes

    Args:
        df (pandas.DataFrame object): data frame

    Returns:
        df (pandas.DataFrame object): data frame
    """

    df = df[df.VISA_CLASS == 'H-1B']
    df = df.drop(columns=['VISA_CLASS'])

    list_cat = ['WAGE_UNIT_OF_PAY', 'PW_SOURCE', 'SOC_NAME',
                'EMPLOYER_STATE', 'WORKSITE_STATE', 'AGENT_REPRESENTING_EMPLOYER']
    for i in list_cat:
        df[i] = df[i].cat.codes
        df[i] = df[i].astype('int')

    return df


def balance_class(df):
    """
    Function that balances CASE_STATUS_CODE.

    The response variable CASE_STATUS_CODE is imbalanced with TRUE:FALSE roughly equal to 7:1.
    This function down-samples the majority class by randomly removing observations
    from the majority class to prevent its signal from dominating the learning algorithm.

    Args:
        df (pandas.DataFrame object): data frame

    Returns:
        df_downsampled (pandas.DataFrame object): downsampled data frame

    """
    # separate observations from each class into different DataFrames
    # resample the majority class without replacement,
    # setting the number of samples to match that of the minority class
    # combine the down-sampled majority class DataFrame with the original minority class DataFrame.

    # Separate majority and minority classes
    df_majority = df[df.CASE_STATUS_CODE == 1]
    df_minority = df[df.CASE_STATUS_CODE == 0]

    # Downsample majority class
    df_majority_downsampled = resample(df_majority,
                                       replace=False,  # sample without replacement
                                       n_samples=78872,  # to match minority class
                                       random_state=123)  # reproducible results

    # Combine minority class with downsampled majority class
    df_downsampled = pd.concat([df_majority_downsampled, df_minority])

    return df_downsampled
