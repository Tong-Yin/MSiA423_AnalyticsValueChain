from lca_app import db
import logging

"""
This module creates LCA prediction database and table using defined db in SQLAlchemy.
Configuration parameter in __init__.py with the schema defined by lca_app.db_model.LCA
"""


def create_db():
    """
    Function that creates initial database

    Args:

    Returns:

    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    create_db()