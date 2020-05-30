import os
from flask import current_app as app

from dotenv import load_dotenv
load_dotenv()

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY") #or"\2\1thisismyscretkey\1\2\e\y\y\h"