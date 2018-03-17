from flask import render_template, request
from src.models import application
from src import rf_prediction as rf
from src import ingest as ingest
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


@application.route('/', methods=['POST','GET'])
def show():

    """View that process a POST with new user input

    :return: redirect to index page
    """

    #return render_template('index.html', result=clf.predict(form1))

    if request.method == "POST":
        # example to get user input
        data = request.form
        result = rf.predict(data)
        if result == 0:
            prediction = "No"
        else:
            prediction = "Yes"
        # prediction = "No" if (result == 0) else "Yes"
        # save user input to db
        ingest.seed_db_single_record(datetime.utcnow(), data, result)
        return render_template('index.html', result=prediction)

    return render_template('index.html')


if __name__ == "__main__":
    application.run()
    #application.run(host='0.0.0.0', debug=True)

