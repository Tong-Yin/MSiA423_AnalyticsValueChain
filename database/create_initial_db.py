from lca_app import db


# Creates a table in the database provided as the 'SQLALCHEMY_DATABASE_URI'
# configuration parameter in __init__.py with the schema defined by model.LCA()

def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    # db.session.close()


if __name__ == "__main__":
   create_db()