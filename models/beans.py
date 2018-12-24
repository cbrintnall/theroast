from sqlalchemy import Table, Column, String, Integer
from application import application

class BeanModel(application.db.Model):
    __tablename__ = "beans"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    color = Column(String(80), nullable=False)

    def repr(self):
        return "<{} | {}>".format(self.name, self.color)
