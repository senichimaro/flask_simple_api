import os
from dotenv import load_dotenv

# grab the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode
DEBUG = True

# Database location
load_dotenv()
APP_DATABASE_URI = os.getenv("APP_DATABASE_URI")
SQLALCHEMY_DATABASE_URI = APP_DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
