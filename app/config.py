import os
from flask import current_app as app

from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
sqldb = "sqlite:///" + os.path.join(basedir, "app.db")

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY") #or"\2\1thisismyscretkey\1\2\e\y\y\h"
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or sqldb
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")