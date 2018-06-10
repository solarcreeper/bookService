#!/usr/bin/python
# -*- coding:utf-8 -*-
from app import get_logger, get_config
import math
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import utils
from app.models import CfgNotify, ConfigJob
from app.main.forms import CfgNotifyForm
from app.utils import query_to_list
from . import main

logger = get_logger(__name__)
cfg = get_config()
PAGE_COUNT = 14

# 通用列表查询
def job_list(view):
    # 接收参数
    action = request.args.get('action')
    id = request.args.get('id')
    page = int(request.args.get('page')) if request.args.get('page') else 1
    length = int(request.args.get('length')) if request.args.get('length') else PAGE_COUNT

    # 删除操作
    if action == 'del' and id:
        pass

    # 查询列表
    query = get_config().JOB_COLLECTION.find().skip((page-1)*PAGE_COUNT).limit(PAGE_COUNT)
    data_list = query_to_list(query)
    total_count = get_config().JOB_COLLECTION.find().count()
    total_page = int(total_count/PAGE_COUNT)

    # # 处理分页
    # if page: query = query.paginate(page, length)

    dict = {'content':data_list, 'total_count': total_count,
            'total_page': total_page, 'page': page, 'length': length}
    return render_template(view, form=dict, current_user=current_user)


# 通用单模型查询&新增&修改
def common_edit(DynamicModel, form, view):
    id = request.args.get('id', '')
    if id:
        # 查询
        model = DynamicModel.get(DynamicModel.id == id)
        if request.method == 'GET':
            utils.model_to_form(model, form)
        # 修改
        if request.method == 'POST':
            if form.validate_on_submit():
                utils.form_to_model(form, model)
                model.save()
                flash('修改成功')
            else:
                utils.flash_errors(form)
    else:
        # 新增
        if form.validate_on_submit():
            model = DynamicModel()
            utils.form_to_model(form, model)
            model.save()
            flash('保存成功')
        else:
            utils.flash_errors(form)
    return render_template(view, form=form, current_user=current_user)


# 根目录跳转
@main.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))


# 首页
@main.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html', current_user=current_user)


# 通知方式查询
@main.route('/jobs', methods=['GET', 'POST'])
@login_required
def jobs():
    return job_list('jobs.html')


# 通知方式配置
@main.route('/templates', methods=['GET', 'POST'])
@login_required
def templates():
    return common_edit(CfgNotify, CfgNotifyForm(), 'templates.html')
