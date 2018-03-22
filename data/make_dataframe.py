# -*- coding: utf-8 -*-
import pandas as pd
from data import data_process_helper as proc


def read_data(path):
    """
    Function that reads in original data.
    This function will read original data into pandas data frame with encoding UTF-8
    while converting certain attributes to avoid parsing issues.

    Args:
        path (str): file path of data, which should be in csv format

    Returns:
        df (pandas.DataFrame object): data frame that holds all data
    """
    df = pd.read_csv(path, delimiter=',', encoding="utf-8",
                     dtype={"EMPLOYER_COUNTRY": str, "EMPLOYER_PROVINCE": str, "EMPLOYER_PHONE": object,
                            "SOC_NAME": str})
    return df


def process_data(df):
    """
    Function that processes input raw data into cleaned and processed data frame.

    Args:
        df (pandas.DataFrame object): data frame that holds raw data

    Returns:
        df (pandas.DataFrame object): data frame that holds processed data
    """
    df = proc.drop_false_predictor(df)
    df = proc.drop_repetitive_predictors(df)
    df = proc.drop_sparse_predictors(df)
    df = proc.drop_irrelevant_predictors(df)
    df = proc.convert_types(df)
    df = proc.impute_missing_cat(df)
    df = proc.add_binary(df)
    df = proc.additional_processing(df)
    df = proc.balance_class(df)
    return df


def make_data_frame(input_filepath):
    """
    Function that transforms raw csv data file to cleaned data frame

    Args:
        input_filepath (str): csv file that holds original data
    Returns:
        processed_df (pandas.DataFrame object):
        final cleaned data frame

    """
    raw_df = read_data(input_filepath)
    processed_df = process_data(raw_df)
    return processed_df
