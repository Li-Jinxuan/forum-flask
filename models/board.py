import time

import hashlib

from sqlalchemy import Column, String

from models import Model, SQLMixin, SQLBase


# class Board(Model):
#     def __init__(self, form):
#         self.id = None
#         self.title = form.get('title', '')
#         self.ct = int(time.time())
#         self.ut = self.ct


class Board(SQLMixin, SQLBase):
    __tablename__ = 'Board'

    title = Column(String(50), nullable=False)

    # def add_default_value(self):
    #     super().add_default_value()
