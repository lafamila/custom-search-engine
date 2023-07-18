from flask import Blueprint, render_template, session, redirect, request
from ..helpers.util_helper import DateUtil
import json
bp = Blueprint('view', __name__, url_prefix='/')

@bp.route('/')
def index_page():
    return render_template('index.html', title="검색엔진")

