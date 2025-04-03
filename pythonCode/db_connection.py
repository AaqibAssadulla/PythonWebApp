from flask_sqlalchemy import SQLAlchemy

database_instance = SQLAlchemy()

def configure_database(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database_instance.init_app(flask_app)
