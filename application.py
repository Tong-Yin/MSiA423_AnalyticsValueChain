from flask import render_template, request
from lca_app import application
from prediction import rf_prediction as rf
from database import ingest as ingest
from datetime import datetime


@application.route('/')
def show():
    """View that displays main page

        Returns:
            flask-obj: rendered html page

    """
    return render_template('index.html')


@application.route('/predict', methods=['POST'])
def submit():
    """View that process a POST with new user input

        Returns:
            flask-obj: rendered html page
    """

    # get user input
    data = request.form

    # call random forest to predict result
    result = rf.predict(data)
    prediction = "No"
    if result == 1:
        prediction = "Yes"

    # save user input to db on RDS
    ingest.seed_db_single_record(datetime.utcnow(), data, result)
    return render_template('result.html', result=prediction)


if __name__ == "__main__":
    application.run()
