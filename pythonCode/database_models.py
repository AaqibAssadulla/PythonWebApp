from flask_sqlalchemy import SQLAlchemy

database_instance = SQLAlchemy()

class UserDetails(database_instance.Model):
    id = database_instance.Column(database_instance.Integer, primary_key=True)
    username = database_instance.Column(database_instance.String(100), unique=True, nullable=False)
    email = database_instance.Column(database_instance.String(150), unique=True, nullable=False)
