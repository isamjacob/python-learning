# Why do we need database 
# Data persists forever
# multiple users can access simultaneously
# Search millions of records in milliseconds
# data is organised and structured

# Types of databases 
# Relational(SQL) and Non-Relational (NoSQL)

# Relational 
# Data in tables, MySQL, PostgreSQL, SQLite
# Used when :
# Structured data, Relationships needed, Financial data, Most backend apps

# Non-Relational (NoSQL)
# Data in documents/JSON, MongoDB, Firebase, Redis, Cassandra
# Used when:
# flexible/changing data, huge scale needed, Real-time apps, Social media feeds

# SQL How it works 

# Database - contains many tables
# Table - like a spreadsheet (rows and columns)
# Row - one record (one student)
# Column - one field (name, age, marks)


import sqlite3
import os

# SQLITE - Build into Python!
# No installation needed

# Connect to database
# Creates file if doesn't exist
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

print("Database connected!")

# Create a table

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        age     INTEGER NOT NULL,
        city    TEXT,
        marks   REAL    DEFAULT 0
    )
""")

conn.commit()
print("Table created!")

# Column types in SQLite:

# INTEGER - whole numbers (1, 2, 100)
# REAL - decimal numbers (85.5, 92.0)
# TEXT - strings ("Sam", "Mumbai")
# BLOB - binary data (images, files)

# Constraints:

# PRIMARY KEY - unique identifier for each row
# AUTOINCREMENT - id increase automatically (1, 2, 3...)
# NOT NULL - this field cannot be empty
# DEFAULT 0 - use 0 if no value provided

# INSERTING DATA

# Insert one record
cursor.execute("""
    INSERT INTO students (name, age, city, marks)
    VALUES (?, ?, ?, ?)
""", ("Sam", 22, "Mumbai", 85.5))

# Insert multiple records at once
students_data = [
    ("Priya", 19, "Delhi", 92.0),
    ("Rahul", 20, "Bangalore", 67.5),
    ("Arjun", 21, "Chennai", 78.0),
    ("Neha",  18, "Mumbai", 95.5),
]

cursor.executemany("""
    INSERT INTO students (name, age, city, marks)
    VALUES (?, ?, ?, ?)
""", students_data)

conn.commit()
print("Data inserted!")

# #  NEVER do this — SQL Injection attack!
# cursor.execute(f"INSERT INTO students VALUES ({name})")

# #  Always use ? placeholders — safe!
# cursor.execute("INSERT INTO students VALUES (?)", (name,))

# SQL Injection is one of the most common security attacks. Always use place holders!


# Reading Data (SELECT):

# Get ALL records
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\n--- All Students ---")
for row in rows:
    print(row)

# Get SPECIFIC columns
cursor.execute("SELECT name, marks FROM students")
rows = cursor.fetchall()

print("\n--- Names and Marks ---")
for row in rows:
    print(f"{row[0]}: {row[1]}")

# Get ONE record
cursor.execute("SELECT * FROM students WHERE id = 1")
row = cursor.fetchone()
print(f"\nStudent 1: {row}")

# Filter with WHERE
cursor.execute("SELECT * FROM students WHERE marks >= 80")
rows = cursor.fetchall()

print("\n--- Students with marks >= 80 ---")
for row in rows:
    print(row)

# ORDER BY
cursor.execute("SELECT * FROM students ORDER BY marks DESC")
rows = cursor.fetchall()

print("\n--- Ranked by marks ---")
for row in rows:
    print(row)

# Updating Data

# Update one record
cursor.execute("""
    UPDATE students
    SET marks = 90.0
    WHERE name = 'Sam'
""")

conn.commit()
print(f"Updated {cursor.rowcount} record(s)")

# Verify update
cursor.execute("SELECT * FROM students WHERE name = 'Sam'")
print(cursor.fetchone())

# Deleting data

# Delete specific record
cursor.execute("DELETE FROM students WHERE name = 'Rahul'")
conn.commit()
print(f"Deleted {cursor.rowcount} record(s)")

# Verify deletion
cursor.execute("SELECT * FROM students")
print("\n--- After deletion ---")
for row in cursor.fetchall():
    print(row)

# Aggregate Functions

# COUNT — how many records
cursor.execute("SELECT COUNT(*) FROM students")
print(f"\nTotal students: {cursor.fetchone()[0]}")

# AVG — average
cursor.execute("SELECT AVG(marks) FROM students")
print(f"Average marks: {cursor.fetchone()[0]:.2f}")

# MAX and MIN
cursor.execute("SELECT MAX(marks), MIN(marks) FROM students")
row = cursor.fetchone()
print(f"Highest: {row[0]}, Lowest: {row[1]}")

# SUM
cursor.execute("SELECT SUM(marks) FROM students")
print(f"Total marks: {cursor.fetchone()[0]}")

# GROUP BY — group results
cursor.execute("""
    SELECT city, COUNT(*), AVG(marks)
    FROM students
    GROUP BY city
""")
print("\n--- By City ---")
for row in cursor.fetchall():
    print(f"City: {row[0]}, Count: {row[1]}, Avg: {row[2]:.2f}")

# Joins - Combining Tables:

# Create a second table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course     TEXT,
        grade      TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
""")

# Insert course data
courses_data = [
    (1, "Python", "A"),
    (1, "DSA", "B"),
    (2, "Python", "A+"),
    (4, "Linux", "B+"),
]

cursor.executemany("""
    INSERT INTO courses (student_id, course, grade)
    VALUES (?, ?, ?)
""", courses_data)

conn.commit()

# INNER JOIN — only matching records
cursor.execute("""
    SELECT students.name, courses.course, courses.grade
    FROM students
    INNER JOIN courses ON students.id = courses.student_id
""")

print("\n--- Student Courses (INNER JOIN) ---")
for row in cursor.fetchall():
    print(f"{row[0]} → {row[1]}: {row[2]}")

# LEFT JOIN — all students even without courses
cursor.execute("""
    SELECT students.name, courses.course, courses.grade
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id
""")

print("\n--- All Students with Courses (LEFT JOIN) ---")
for row in cursor.fetchall():
    print(f"{row[0]} → {row[1]}: {row[2]}")

# Always close connnection

conn.close()
print("\nDatabase connection closed!")