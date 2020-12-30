import time
from sqlalchemy import Column, String, Integer, Text

from models import Model, SQLMixin, SQLBase


# class Reply(Model):
#     def __init__(self, form):
#         self.id = None
#         self.content = form.get('content', '')
#         self.ct = int(time.time())
#         self.ut = self.ct
#         self.topic_id = int(form.get('topic_id', -1))
#
#     def user(self):
#         from .user import User
#         u = User.find(self.user_id)
#         return u

class Reply(SQLMixin, SQLBase):
    __tablename__ = 'Reply'

    content = Column(Text, nullable=False)
    topic_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    def user(self):
        from .user import User

        u = User.one(id=self.user_id)
        return u
