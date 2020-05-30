from flask import Blueprint, render_template
from flask import current_app as app


#Configure Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def index():
    #homepage
    return render_template('home/home.html', title="Flask Home")
