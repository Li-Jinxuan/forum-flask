from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    Response, json)

from models.mail import Mail
from routes import *

from models.reply import Reply

main = Blueprint('reply', __name__)


def users_from_content(content):
    # 内容 @123 内容
    # 如果用户名含有空格 就不行了 @name 123
    parts = content.split(' ')
    users = []

    for p in parts:
        if p.startswith('@'):
            username = p[1:]
            u = User.one(username=username)
            users.append(u)

    return users


def send_mails(sender, receivers, content):
    for r in receivers:
        form = dict(
            title='你被 {} AT 了'.format(sender.username),
            content=content,
            sender_id=sender.id,
            receiver_id=r.id
        )
        Mail.new(form)


@main.route("/add", methods=["POST"])
def add():
    form = request.json
    u = current_user()
    # @功能
    content = form['content']
    users = users_from_content(content)
    send_mails(u, users, content)

    form['user_id'] = u.id
    m = Reply.new(**form)
    form['created_time'] = m.created_time
    form['username'] = User.one(id=u.id).username
    return Response(json.dumps(form))

# @main.route("/add", methods=["POST"])
# def add():
#     form = request.form.to_dict()
#     u = current_user()
#     form['user_id'] = u.id
#     # m = Reply.new(form, user_id=u.id)
#     m = Reply.new(**form)
#     return redirect(url_for('topic.detail', id=m.topic_id))
