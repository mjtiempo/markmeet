import qrcode
from base64 import b64encode
from io import BytesIO
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import current_app as app
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from ..forms import LoginForm, SignUpForm
from ..models import User, Qrcode
from .. import db

#Configure Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET'])
def login():
    #login form
    form = LoginForm()
    return render_template('auth/login.html', title="Login", form=form)

@auth_bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password_hash, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('user.profile'))

@auth_bp.route('/signup', methods=['GET'])
def signup():
    form = SignUpForm()
    return render_template('auth/signup.html', form=form)
    
@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, first_name=first_name, last_name=last_name, password_hash=generate_password_hash(password, method='sha256'))
    

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    #get newly registered user and create a qrcode
    user = User.query.filter_by(email=email).first()
    qrcode_data = '{} {} {} registered {}'.format(user.first_name, user.last_name, user.email, str(datetime.utcnow()))

    img = qrcode.make(qrcode_data)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = b64encode(buffered.getvalue())
    img_base64 = bytes("data:image/png;base64,", encoding='utf-8') + img_str
    new_qrcode = Qrcode(user_id=user.id, body=img_base64.decode())
    db.session.add(new_qrcode)
    db.session.commit()

    flash('{}, registered successfully!'.format(new_user))
    return redirect(url_for('auth.login'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))