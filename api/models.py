# models.py

# DATABASE MODELS

from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Student(Base):
    __tablename__ = "students"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String, nullable=False)
    email      = Column(String, unique=True, nullable=False)
    age        = Column(Integer)
    city       = Column(String)
    marks      = Column(Float, default=0)
    is_active  = Column(Boolean, default=True)