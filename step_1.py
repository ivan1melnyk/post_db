from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql://myuser:mysecretpassword@localhost:5432/universitydb')

# Creating session
Session = sessionmaker(bind=engine)
session = Session()

# Base class for models
Base = declarative_base()


# Student table
class Student(Base):
    __tablename__ = "students"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(50), nullable=False)
    group_id: int = Column(Integer, nullable=False)


# Group table
class Group(Base):
    __tablename__ = "groups"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(50), nullable=False)


# Teacher table
class Teacher(Base):
    __tablename__ = "teachers"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(50), nullable=False)


# Subject table with teacher reference
class Subject(Base):
    __tablename__ = "subjects"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(50), nullable=False)
    teacher_id: int = Column(Integer, ForeignKey('teachers.id'))


# Grade table
class Grade(Base):
    __tablename__ = "grades"
    id: int = Column(Integer, primary_key=True)
    student_id: int = Column(Integer, ForeignKey(
        'students.id'))
    subject_id: int = Column(Integer, ForeignKey(
        'subjects.id'))
    grade: int = Column(Integer, nullable=False)
    date_received: datetime = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)
Base.metadata.bind = engine
