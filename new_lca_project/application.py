from flask import render_template, request
from lca_app import application
from prediction import rf_prediction as rf
from database import ingest as ingest
from datetime import datetime

# @application.route('/')
# def index():
#
#     """Main view that displays the survey form to predict LCA status
#
#     :return: rendered html template
#
#     """
#     #make dataset
#     #seed db
#
#     return render_template('index.html')


@application.route('/predict', methods=['POST'])
def submit():
    # example to get user input
    data = request.form
    result = rf.predict(data)
    prediction = "No"
    if result == 1:
        prediction = "Yes"
    # save user input to db
    ingest.seed_db_single_record(datetime.utcnow(), data, result)
    return render_template('result.html', result=prediction)


@application.route('/')
def show():

    """View that process a POST with new user input

    :return: redirect to index page
    """
    return render_template('index.html')


if __name__ == "__main__":
    application.run()
