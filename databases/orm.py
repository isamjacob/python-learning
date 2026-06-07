# SQLAlchemy ORM
# ORM = Object Relational Mapper
# Without ORM = you write raw SQL:

# cursor.execute("SELECT * FROM students WHERE marks >= 80")
# rows = cursor.fetchall()

# With ORM - you write Python:

# students = session.query(Student).filter(Student.marks >= 80).all()

# Same result - but Python instead of SQL strings!

# Why ORM
# Write Python instead of SQL
# Less error-prone — no typos in SQL strings
# Works with ANY database — SQLite, PostgreSQL, MySQL
# Security built in — no SQL injection
# Used in EVERY real Python project

# Setting up SQLAlchemy:

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine - connects to database
engine = create_engine("sqlite:///school_orm.db", echo=False)
# echo=True shows SQL being executed (useful for debugging)

# Base class for all models
Base = declarative_base()

# Create session factory
Session = sessionmaker(bind=engine)
session = Session()

print("SQLAlchemy connected!")

# Creating Models (Tables as Classses)

# MODELS - Tables as Classes

class Student(Base):
    __tablename__ = "students"  # table name in database

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String)
    marks = Column(Float, default=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Students(id={self.id}, name={self.name}, marks={self.marks})"

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    duration = Column(Integer)
    instructor = Column(String)

    def __repr__(self):
        return f"Course(id={self.id}, name={self.name})"
    
# Create all tables in database
Base.metadata.create_all(engine)
print("Tables created!")

# Insert - Adding records:

# Create student objects
student1 = Student(name="Sam",   age=22, city="Mumbai",    marks=85.5)
student2 = Student(name="Priya", age=19, city="Delhi",     marks=92.0)
student3 = Student(name="Rahul", age=20, city="Bangalore", marks=67.5)
student4 = Student(name="Arjun", age=21, city="Chennai",   marks=78.0)
student5 = Student(name="Neha",  age=18, city="Mumbai",    marks=95.5)

# Add to session
session.add(student1)          # add one
session.add_all([student2, student3, student4, student5])  # add many

# Commit to save
session.commit()
print("Students added!")

# Add courses
course1 = Course(name="Python",     duration=8,  instructor="Mr. Kumar")
course2 = Course(name="DSA",        duration=12, instructor="Ms. Sharma")
course3 = Course(name="Networking", duration=6,  instructor="Mr. Patel")

session.add_all([course1, course2, course3])
session.commit()
print("Courses added!")

# Select - Reading records

# Get ALL students
students = session.query(Student).all()
print("\n--- All Students ---")
for student in students:
    print(student)

# Get FIRST student
first = session.query(Student).first()
print(f"\nFirst: {first}")

# Get by ID
student = session.query(Student).get(1)
print(f"\nID 1: {student}")

# Filter — WHERE clause
top_students = session.query(Student)\
    .filter(Student.marks >= 80)\
    .all()

print("\n--- Top Students (marks >= 80) ---")
for s in top_students:
    print(s)

# Filter with multiple conditions
mumbai_toppers = session.query(Student)\
    .filter(Student.city == "Mumbai")\
    .filter(Student.marks >= 80)\
    .all()

print("\n--- Mumbai students with marks >= 80 ---")
for s in mumbai_toppers:
    print(s)

# ORDER BY
ranked = session.query(Student)\
    .order_by(Student.marks.desc())\
    .all()

print("\n--- Ranked by marks ---")
for s in ranked:
    print(f"{s.name}: {s.marks}")

# COUNT
total = session.query(Student).count()
print(f"\nTotal students: {total}")

# LIMIT
top3 = session.query(Student)\
    .order_by(Student.marks.desc())\
    .limit(3)\
    .all()

print("\n--- Top 3 students ---")
for s in top3:
    print(s)

# Update - Modifying Records

# Update one record
student = session.query(Student).filter(Student.name == "Sam").first()
student.marks = 90.0
student.city  = "Pune"
session.commit()
print(f"\nUpdated Sam: {student}")

# Update multiple records
session.query(Student)\
    .filter(Student.city == "Mumbai")\
    .update({"is_active": False})
session.commit()
print("Updated all Mumbai students!")

# DELETE - Removing Records

# Delete one record
student = session.query(Student).filter(Student.name == "Rahul").first()
session.delete(student)
session.commit()
print(f"\nDeleted Rahul")

# Verify
remaining = session.query(Student).all()
print("Remaining students:")
for s in remaining:
    print(s)

# Useful Queries

# Check if exists
exists = session.query(Student)\
    .filter(Student.name == "Sam")\
    .first() is not None
print(f"\nSam exists: {exists}")

# Get specific columns only
names = session.query(Student.name, Student.marks).all()
print("\n--- Names and marks ---")
for name, marks in names:
    print(f"{name}: {marks}")

# Average marks
from sqlalchemy import func
avg = session.query(func.avg(Student.marks)).scalar()
print(f"\nAverage marks: {avg:.2f}")

# Max and min
max_marks = session.query(func.max(Student.marks)).scalar()
min_marks = session.query(func.min(Student.marks)).scalar()
print(f"Highest: {max_marks}, Lowest: {min_marks}")

# Group by city
city_stats = session.query(
    Student.city,
    func.count(Student.id),
    func.avg(Student.marks)
).group_by(Student.city).all()

print("\n--- Stats by city ---")
for city, count, avg in city_stats:
    print(f"{city}: {count} students, avg marks: {avg:.2f}")

# Closing session:

session.close()
print("\nSession closed!")