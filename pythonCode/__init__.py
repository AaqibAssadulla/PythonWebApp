from flask import Flask
from pythonCode.web_routes import web_blueprint  # Import routes
#from pythonCode.db_connection import configure_database  # Import database setup

def initialize_web_app():
    flask_app = Flask(__name__, static_folder='../src/assets', template_folder='../src/html')

    # Database initialization (if using PostgreSQL)
    #configure_database(flask_app)

    # Register routes
    flask_app.register_blueprint(web_blueprint)

    return flask_app
