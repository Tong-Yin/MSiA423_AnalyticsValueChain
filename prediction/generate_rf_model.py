"""

This module generates a trained random forest classifier and saves it in a pickle file.

"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import numpy as np
from data import make_dataframe as mk


def generate_rf(df):
    """
    Function that generates a trained random forest classifier

    Args:
        df (pandas.DataFrame object): data frame that contains cleaned data

    Returns:
        clf (Random Forest Classifier): random forest object
    """
    # retrieve data frame from csv

    # extract predictors
    predictors = df.loc[:, ['TOTAL_WORKERS',
                            'NEW_EMPLOYMENT',
                            'CONTINUED_EMPLOYMENT',
                            'CHANGE_PREVIOUS_EMPLOYMENT',
                            'NEW_CONCURRENT_EMPLOYMENT',
                            'CHANGE_EMPLOYER',
                            'AMENDED_PETITION',
                            'FULL_TIME_POSITION_CODE',
                            'H1B_DEPENDENT_CODE',
                            'WILLFUL_VIOLATOR_CODE',
                            'WAGE_UNIT_OF_PAY',
                            'PREVAILING_WAGE',
                            'WAGE_RATE_OF_PAY_FROM',
                            'WAGE_RATE_OF_PAY_TO']]


    # set random seed
    np.random.seed(0)

    # split data frame into train and test sets
    # train, test = tr.split_into_train_test(df)

    # get train and test features and target variables and slice data
    # train_features = tr.extract_predictors(train)
    # train_target = train['case_status_code']
    # test_features = tr.extract_predictors(test)
    # test_target = test['case_status_code']

    # generate target variables
    target = df['CASE_STATUS_CODE']

    # train a random forest Classifier
    clf = RandomForestClassifier(n_estimators=5, random_state=0)
    clf.fit(predictors, target)

    # apply the Classifier we trained to the test data
    # clf.predict(test_features)

    # evaluate Classifier
    # predictions = df.target_names[clf.predict(test_features)]

    # create confusion matrix
    # pd.crosstab(test['case_status_code'], predictions, rownames=['Actual'], colnames=['Predicted'])

    # view a list of the features and their importance scores
    # list(zip(train_features, clf.feature_importances_))

    return clf


if __name__ == "__main__":
    df = mk.make_data_frame('H-1B_Data_FY17.csv')
    clf = generate_rf(df)
    joblib.dump(clf, open('rf_model.pkl', 'wb'))