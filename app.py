from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from models import db

def create_app(test_config=None):
    '''
    "instance_relative_config"
    enable relative path within project scoop
    Here __name__is the name of the current Python module
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    # Database Connection 
    db.init_app(app)
    migrate = Migrate(app, db)

    CORS(app)

    @app.route('/')
    @cross_origin()
    def index():
        return jsonify({"message":"App Running"})

    # Return the app instance
    return app
