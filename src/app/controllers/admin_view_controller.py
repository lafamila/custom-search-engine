from flask import Blueprint, render_template, session, redirect, request, make_response
from ..helpers.util_helper import DateUtil
from ..helpers import admin_helper
import json
bp = Blueprint('admin_view', __name__, url_prefix='/admin')

@bp.route('/')
def index_page():
    return render_template('/admin/index.html')

@bp.route('/login')
def login_page():
    return render_template('/admin/login.html')

@bp.route('/setting')
@admin_helper.admin_session_check
def setting_page():
    return render_template('/admin/setting.html')

@bp.route('/logout')
@admin_helper.admin_session_clear
def logout_page():
    return redirect('/admin/login')
