from flask import Blueprint, render_template
from flask import current_app as app
from ..forms import LoginForm


#Configure Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET'])
def login():
    #login form
    form = LoginForm()
    return render_template('auth/login.html', title="Login", form=form)