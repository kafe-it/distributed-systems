from sqlalchemy import Column, Integer, String
from database.database import Base


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    todo = Column(String(255), index=True)
