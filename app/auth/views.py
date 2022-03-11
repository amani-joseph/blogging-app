'''
CONTROLS THE LOGIN TEMPLATES

THE SIGN UP FUNCTIONALITY SEND THE EMAIL YOU MAY WISH TO DISCONNECT THAT IF YOU DONT WANT TO IMPLEMENT A SIGN UP EMAIL
'''


# from flask import render_template,url_for,flash,redirect,request
# from flask_login import login_user, logout_user, login_required
# from . import auth
# from ..models import User
# from .forms import RegForm,LoginForm
# from .. import db
# from ..email import mail_message

# @auth.route('/login', methods = ['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username = form.username.data).first()
#         if user != None and user.verify_password(form.password.data):
#             login_user(user,form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))
#         flash('Invalid username or Password')
#     return render_template('auth/login.html', loginform = form)

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("main.index"))

# @auth.route('/signup', methods = ["GET","POST"])
# def signup():
#     form = RegForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data, password = form.password.data)
#         user.save_u()
#         mail_message("Welcome to '<<My app name>>'","email/welcome_user",user.email,user=user)
#         return redirect(url_for('auth.login'))
#     return render_template('auth/register.html', r_form = form)