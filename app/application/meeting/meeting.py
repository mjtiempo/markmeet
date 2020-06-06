import os
from flask import Blueprint, render_template, request
from flask import current_app as app
from flask_login import login_required, current_user
from ..models import User
from ..utils import generate_token

#Configure Blueprint
meeting_bp = Blueprint('meeting', __name__)

@meeting_bp.route('/meeting', methods=['GET'])
def index():
    name = "Guest"
    if current_user.is_authenticated:
        user = User.query.get(current_user.get_id())
        name = "{} {}".format(user.first_name, user.last_name)
    return render_template('meeting/index.html', title="Setup Meeting", name=name)

@meeting_bp.route('/meeting', methods=['POST'])
@login_required
def start_meeting():
    user = User.query.get(current_user.get_id())
    name = "{} {}".format(user.first_name, user.last_name)
    appid = os.getenv("JWT_APP_ID") 
    appkey = os.getenv("JWT_APP_KEY") 
    domain = os.getenv("JITSI_DOMAIN") 
    audience = domain
    room = request.form.get('roomname')
    jwtoken = generate_token(name, user.email, room, appid, appkey, domain, audience, avatar=None)
    title = room + " Meeting"
    return render_template('meeting/meeting.html', title=title, domain=domain, roomname=room, jwt=jwtoken)

@meeting_bp.route('/meeting/join', methods=['POST'])
def guest_meeting():
    room = request.form.get('roomname')
    domain = os.getenv("JITSI_DOMAIN")
    title = room + " Meeting"
    return render_template('meeting/meeting.html', title=title, domain=domain, roomname=room)


