"""

This module creates the LCA data model for the database to be setup for the app.

"""

from lca_app import db


class LCA(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    employer_name = db.Column(db.String(100), unique=False, nullable=False)
    employer_state = db.Column(db.String(2), unique=False, nullable=False)
    worksite_state = db.Column(db.String(2), unique=False, nullable=False)
    total_workers = db.Column(db.Integer, unique=False, nullable=False)
    new_employment = db.Column(db.Boolean, unique=False, nullable=False)
    continued_employment = db.Column(db.Boolean, unique=False, nullable=False)
    change_previous_employment = db.Column(db.Boolean, unique=False, nullable=False)
    new_concurrent_employment = db.Column(db.Boolean, unique=False, nullable=False)
    change_employer = db.Column(db.Boolean, unique=False, nullable=False)
    amended_petition = db.Column(db.Boolean, unique=False, nullable=False)
    prevailing_wage = db.Column(db.Float, unique=False, nullable=False)
    wage_rate_of_pay_from = db.Column(db.Float, unique=False, nullable=False)
    wage_rate_of_pay_to = db.Column(db.Float, unique=False, nullable=False)
    wage_unit_of_pay = db.Column(db.Integer, unique=False, nullable=False)
    full_time_position_code = db.Column(db.Boolean, unique=False, nullable=False)
    h1b_dependent_code = db.Column(db.Boolean, unique=False, nullable=False)
    willful_violator_code = db.Column(db.Boolean, unique=False, nullable=False)
    case_status_code = db.Column(db.Boolean, unique=False, nullable=False)


    def __repr__(self):
        return '<LCA case status predicted to be %r>' % str(self.case_status_code)