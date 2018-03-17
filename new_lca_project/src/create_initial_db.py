from src.models import db
from src.models.db_model import LCA
from src.data import make_dataframe as mk
from src.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine

# Creates a table in the database provided as the 'SQLALCHEMY_DATABASE_URI'
# configuration parameter in __init__.py with the schema defined by model.LCA()

def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    # db.session.close()


if __name__ == "__main__":
   create_db()