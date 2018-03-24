"""Ingestion module

This module is meant to be called to ingest data and place it into db. Once an API is used
the module can be extended with a function that calls the API and puts the data into the db.

Functionality presumes that the db has already been created.

"""

from numpy.distutils.fcompiler import str2bool

from lca_app import db
from lca_app.db_model import LCA


def seed_db_single_record(primary_key, record, result):

    """Seed a preexisting db with data

    Returns:

    """

    new_lca = LCA(
        id = primary_key,
        employer_name = record['employer_name'],
        employer_state = record['employer_state'],
        worksite_state = record['worksite_state'],
        total_workers = int(record['total_workers']),
        new_employment = str2bool(record['new_employment']),
        continued_employment = str2bool(record['continued_employment']),
        change_previous_employment = str2bool(record['change_previous_employment']),
        new_concurrent_employment = str2bool(record['new_concurrent_employment']),
        change_employer = str2bool(record['change_employer']),
        amended_petition = str2bool(record['amended_petition']),
        prevailing_wage = float(record['prevailing_wage']),
        wage_rate_of_pay_from = float(record['wage_rate_of_pay_from']),
        wage_rate_of_pay_to = float(record['wage_rate_of_pay_to']),
        wage_unit_of_pay = int(record['wage_unit_of_pay']),
        full_time_position_code = str2bool(record['full_time_position_code']),
        h1b_dependent_code = str2bool(record['h1b_dependent_code']),
        willful_violator_code = str2bool(record['willful_violator_code']),
        case_status_code = str2bool(result)
    )
    db.session.add(new_lca)
    db.session.commit()

# def seed_db(df):
#     df = df['EMPLOYER_NAME', 'EMPLOYER_STATE', 'WORKSITE_STATE',
#             'SOC_NAME', 'TOTAL_WORKERS', 'NEW_EMPLOYMENT', 'CONTINUED_EMPLOYMENT',
#             'CHANGE_PREVIOUS_EMPLOYMENT', 'NEW_CONCURRENT_EMPLOYMENT',
#             'CHANGE_EMPLOYER', 'AMENDED_PETITION',
#             'PREVAILING_WAGE', 'PW_SOURCE', 'WAGE_RATE_OF_PAY_FROM',
#             'WAGE_RATE_OF_PAY_TO', 'WAGE_UNIT_OF_PAY',
#             'FULL_TIME_POSITION_CODE', 'H1B_DEPENDENT_CODE', 'WILLFUL_VIOLATOR_CODE', 'CASE_STATUS_CODE']
#
#     for index, row in df.iterrows():
#         seed_db_single_record(index, row)