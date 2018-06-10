#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, request, url_for, flash
from app import get_config
from . import auth
from .forms import LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_config().USERS_COLLECTION.find_one({'username': form.username.data})
        if user is not None and User.validate_login(user['password'], form.password.data):
            login_user(User(user['username']))
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出登录')
    return redirect(url_for('auth.login'))
