from flask import Blueprint, render_template, session, redirect, request
from ..helpers.util_helper import DateUtil
import json
bp = Blueprint('admin_view', __name__, url_prefix='/admin')

@bp.route('/')
def index_page():
    return render_template('/admin/index.html')

@bp.route('/login')
def login_page():
    return render_template('/admin/login.html')

