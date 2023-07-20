from flask import Blueprint, session, make_response, request, jsonify, g
from ..helpers.util_helper import DateUtil
from ..helpers.database_helper import DB
from ..helpers import admin_helper
import json
bp = Blueprint('admin_api', __name__, url_prefix='/api/admin')

@bp.before_request
def connect():
    g.db = DB()
    g.curs = g.db.cursor()

@bp.after_request
def disconnect(response):
    if response.status_code != 500:
        g.db.commit()

    g.curs.close()
    g.db.close()
    return response


@bp.route('/login', methods=['POST'])
def login():
    params = request.form.to_dict()
    row = g.curs.execute("SELECT * FROM user WHERE user_id=%(user_id)s AND user_pw=password(%(user_pw)s)", params)
    if row:
        user = g.curs.fetchone()
        session["member"] = user["user_sn"]
        return jsonify({"status": True, "message": "성공적으로 가입되었습니다."})
    else:
        return jsonify({"status": False, "message": "로그인 정보가 일치하지 않습니다."})

@bp.route('/join', methods=['POST'])
def join():
    params = request.form.to_dict()
    row = g.curs.execute("SELECT * FROM user WHERE user_id=%(new_user_id)s", params)
    if row:
        return jsonify({"status": False, "message": "이미 존재하는 아이디입니다."})
    else:
        g.curs.execute("INSERT INTO user(user_id, user_pw) VALUES(%(new_user_id)s, password(%(new_user_pw)s))", params)
        return jsonify({"status" : True, "message":"성공적으로 가입되었습니다."})


@bp.route('/logout', methods=['GET','POST'])
@admin_helper.admin_session_clear
def logout_page():
    return make_response(json.dumps(dict()), 200)
