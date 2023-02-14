from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from random import *
# from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import time
import os

auth = Blueprint('auth', __name__)
otp=randint(000000,999999)
# s = URLSafeTimedSerializer('Thisisasecret!')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')

        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                # flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                flash(user.first_name)
                return redirect(url_for('links.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # email = request.form['email']

            msg = Message('Confirm Email', sender='mofei.shi1@gmail.com', recipients=[email])
            # global otp

            
            msg.body = 'Your otp is {}'.format(otp)
            # from . import app
            # mail=Mail(app)
            from . import mail
            mail.send(msg)
            global new_user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))#, income =-1)
            return render_template('verify.html')
            # flash('The email you entered is {}. The token is {}'.format(email, token))            
    return render_template("sign_up.html", user=current_user)
            
            
            
@auth.route('/validate', methods=["POST"])
def validate():
    user_otp=request.form['otp']
    if otp == int(user_otp):

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Account created for {}'.format(new_user.first_name), category='success')
        return redirect(url_for('links.dashboard', user=current_user))

    else:
        flash("The OTP you entered was incorrect, please try again", category='error')
    return render_template("sign_up.html", user=current_user)
