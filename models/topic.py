import time
from sqlalchemy import Column, String, Integer, Text

from models import Model, SQLMixin, SQLBase


# class Topic(Model):
#     @classmethod
#     def get(cls, id):
#         m = cls.find_by(id=id)
#         m.views += 1
#         m.save()
#         return m
#
#     def __init__(self, form):
#         self.id = None
#         self.views = 0
#         self.title = form.get('title', '')
#         self.content = form.get('content', '')
#         self.ct = int(time.time())
#         self.ut = self.ct
#         self.user_id = form.get('user_id', '')
#         self.board_id = int(form.get('board_id', -1))
#
#     def replies(self):
#         from .reply import Reply
#         ms = Reply.find_all(topic_id=self.id)
#         return ms
#
#     def board(self):
#         from .board import Board
#         m = Board.find(self.board_id)
#         return m
#
#     def user(self):
#         from .user import User
#         u = User.find(self.user_id)
#         return u

class Topic(SQLMixin, SQLBase):
    __tablename__ = 'Topic'

    views = Column(Integer, nullable=False)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(String(50), nullable=False)
    board_id = Column(String(50), nullable=False, default=-1)

    @classmethod
    def get(cls, id):
        m = cls.one(id=id)
        m.views += 1
        # query = dict(
        #     views=m.views
        # )
        # cls.update(m.id, query)
        return m

    def replies(self):
        from .reply import Reply
        ms = Reply.all(topic_id=self.id)
        return ms

    def board(self):
        from .board import Board
        m = Board.one(id=self.board_id)
        return m

    def user(self):
        from .user import User
        u = User.one(id=self.user_id)
        return u
