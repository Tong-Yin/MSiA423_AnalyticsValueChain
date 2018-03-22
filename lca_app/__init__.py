from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prediction import generate_rf_model as gm

# needed by beanstalk
application = Flask(__name__)

# SQLAlchemy configuration (can update with AWS RDS settings)
application.config.from_pyfile('../config.py', silent=True)

# Initialize the database
db = SQLAlchemy(application)


clf = gm.load_rf_model()