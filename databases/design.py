# Database Design 

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

engine = create_engine("sqlite:///school_design.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# PROPERLY DESIGNED TABLES

class Department(Base):
    __tablename__ = "departments"

    id   = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    code = Column(String, nullable=False)

    # relationship — access teachers directly from department
    teachers = relationship("Teacher", back_populates="department")

    def __repr__(self):
        return f"Department({self.name})"


class Teacher(Base):
    __tablename__ = "teachers"

    id            = Column(Integer, primary_key=True, autoincrement=True)
    name          = Column(String, nullable=False)
    email         = Column(String, unique=True)
    department_id = Column(Integer, ForeignKey("departments.id"))

    # relationships
    department = relationship("Department", back_populates="teachers")
    courses    = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"Teacher({self.name})"


class Student(Base):
    __tablename__ = "students"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String, nullable=False)
    email      = Column(String, unique=True)
    age        = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now)

    # relationship
    enrollments = relationship("Enrollment", back_populates="student")

    def __repr__(self):
        return f"Student({self.name})"


class Course(Base):
    __tablename__ = "courses"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String, nullable=False)
    duration   = Column(Integer)   # weeks
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    # relationships
    teacher     = relationship("Teacher", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")

    def __repr__(self):
        return f"Course({self.name})"


# Many to Many — students and courses
# Junction table (enrollment)
class Enrollment(Base):
    __tablename__ = "enrollments"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id  = Column(Integer, ForeignKey("courses.id"))
    marks      = Column(Float, default=0)
    enrolled_at = Column(DateTime, default=datetime.datetime.now)

    # relationships
    student = relationship("Student", back_populates="enrollments")
    course  = relationship("Course",  back_populates="enrollments")

    def __repr__(self):
        return f"Enrollment(student={self.student_id}, course={self.course_id})"


# Create all tables
Base.metadata.create_all(engine)
print("Tables created!")

# INSERT DATA

# Departments
dept1 = Department(name="Computer Science", code="CS")
dept2 = Department(name="Mathematics", code="MATH")
session.add_all([dept1, dept2])
session.commit()

# Teachers
teacher1 = Teacher(name="Mr. Kumar",  email="kumar@school.com",  department_id=1)
teacher2 = Teacher(name="Ms. Sharma", email="sharma@school.com", department_id=1)
teacher3 = Teacher(name="Mr. Patel",  email="patel@school.com",  department_id=2)
session.add_all([teacher1, teacher2, teacher3])
session.commit()

# Students
student1 = Student(name="Sam",   email="sam@gmail.com",   age=22)
student2 = Student(name="Priya", email="priya@gmail.com", age=19)
student3 = Student(name="Rahul", email="rahul@gmail.com", age=20)
session.add_all([student1, student2, student3])
session.commit()

# Courses
course1 = Course(name="Python",     duration=8,  teacher_id=1)
course2 = Course(name="DSA",        duration=12, teacher_id=1)
course3 = Course(name="Networking", duration=6,  teacher_id=2)
session.add_all([course1, course2, course3])
session.commit()

# Enrollments (many to many)
e1 = Enrollment(student_id=1, course_id=1, marks=85.0)
e2 = Enrollment(student_id=1, course_id=2, marks=78.0)
e3 = Enrollment(student_id=2, course_id=1, marks=92.0)
e4 = Enrollment(student_id=3, course_id=3, marks=88.0)
session.add_all([e1, e2, e3, e4])
session.commit()
print("Data inserted!")

# QUERYING WITH RELATIONSHIPS

# Get all courses for a student
print("\n--- Sam's courses ---")
sam = session.query(Student).filter(Student.name == "Sam").first()
for enrollment in sam.enrollments:
    print(f"{enrollment.course.name}: {enrollment.marks}")

# Get all students in a course
print("\n--- Python course students ---")
python = session.query(Course).filter(Course.name == "Python").first()
for enrollment in python.enrollments:
    print(f"{enrollment.student.name}: {enrollment.marks}")

# Get all teachers in a department
print("\n--- CS Department teachers ---")
cs = session.query(Department).filter(Department.name == "Computer Science").first()
for teacher in cs.teachers:
    print(teacher.name)

# Get teacher for a course
print("\n--- Python course teacher ---")
print(python.teacher.name)

session.close()