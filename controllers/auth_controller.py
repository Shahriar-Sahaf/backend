from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()  # بارگذاری کاربر از پایگاه داده
        
        if user and user.password == password:  # بررسی رمز عبور
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))