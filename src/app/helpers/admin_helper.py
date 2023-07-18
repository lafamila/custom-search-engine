from functools import wraps
from flask import request, make_response, current_app, redirect, session

def admin_session_check(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if "member" in session:
            return func(*args, **kwargs)
        else:
            return redirect('/login')
    return wrap