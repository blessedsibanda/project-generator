from flask import (Blueprint, flash, render_template, 
    request, redirect, url_for)
from flask_login import login_user, logout_user

from webapp import db  
from .forms import LoginForm, RegisterForm
from .models import User

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    static_folder='../static',
    url_prefix='/auth'
)

@auth_blueprint.route('login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, remember=form.remember.data)
        flash('Login successful.', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)

@auth_blueprint.route('register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.email = form.email.data    
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()  
        flash('Registration successful, you can now login', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_blueprint.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.index'))