from flask import Blueprint, render_template
from flask import current_app as app
from flask_login import login_required, current_user
from ..models import User
from .. import login_manager


#required for flask-login
@login_manager.user_loader
def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

#Configure Blueprint
user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['GET'])
@login_required
def profile():
    #user index
    user = load_user(current_user.get_id())
    name = "{} {}".format(user.first_name, user.last_name)
    return render_template('user/profile.html', title="Profile", name=name)