import uuid
from functools import wraps

from flask import session, request, abort

from models.user import User


def current_user():
    # 从 session 中找到 user_id 字段, 找不到就 -1
    # 然后 User.find_by 来用 id 找用户
    # 找不到就返回 None
    if 'user_id' in session:
        uid = int(session['user_id'])
        e = User.exist(id=uid)
        if e:
            return User.one(id=uid)
        else:
            return None
    else:
        return None



csrf_tokens = dict()


def csrf_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        u = current_user()
        if token in csrf_tokens and csrf_tokens[token] == u.id:
            csrf_tokens.pop(token)
            return f(*args, **kwargs)
        else:
            abort(401)

    return wrapper


def new_csrf_token():
    u = current_user()
    token = str(uuid.uuid4())
    csrf_tokens[token] = u.id
    return token
