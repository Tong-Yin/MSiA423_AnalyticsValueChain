from flask import render_template, request
from lca_app import application
from prediction import rf_prediction as rf
from database import ingest as ingest
from datetime import datetime
import logging


@application.route('/')
def show():
    """View that displays main page

        Returns:
            flask-obj: rendered html page

    """
    logger.info('Visiting main page.')
    return render_template('index.html')


@application.route('/predict', methods=['POST'])
def submit():
    """View that process a POST with new user input

        Returns:
            flask-obj: rendered html page
    """
    try:
        # get user input
        data = request.form
        # logging
        logger.info('Got user input.')
        # call random forest to predict result
        result = rf.predict(data)
        prediction = "No"
        if result == 1:
            prediction = "Yes"
    except:
        logger.warning('Missing or invalid user inputs resulting in prediction failure.')
    try:
        # save user input to db on RDS
        ingest.seed_db_single_record(datetime.utcnow(), data, result)
        logger.info('Saved user input in RDS database.')
    except:
        logger.warning('Unsuccessful connection to RDS database caused failure in data ingestion.')

    return render_template('result.html', result=prediction)


if __name__ == "__main__":
    # logger initialization
    logging.basicConfig(filename='application.log', level=logging.INFO)
    logger = logging.getLogger(__name__)
    application.run()
