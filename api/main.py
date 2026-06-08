# main.py

# FASTAPI - MAIN APPLICATION

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Student Management API",
    description="A REST API for managing students",
    version="1.0.0"
)


# ROOT ENDPOINT

@app.get("/")
def root():
    return {"message": "Welcome to Student API!"}


# GET ALL STUDENTS

@app.get("/students", response_model=List[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students


# GET STUDENT BY ID

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# CREATE STUDENT

@app.post("/students", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new student
    new_student = models.Student(
        name  = student.name,
        email = student.email,
        age   = student.age,
        city  = student.city,
        marks = student.marks
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)   # refresh to get auto-generated id
    return new_student


# UPDATE STUDENT

@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student_data: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update only provided fields
    update_data = student_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student


# DELETE STUDENT

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return {"message": f"Student {student_id} deleted successfully"}


# SEARCH STUDENTS

@app.get("/students/search/{name}", response_model=List[schemas.StudentResponse])
def search_students(name: str, db: Session = Depends(get_db)):
    students = db.query(models.Student).filter(
        models.Student.name.contains(name)
    ).all()
    return students


# GET TOP STUDENTS

@app.get("/students/top/{limit}", response_model=List[schemas.StudentResponse])
def get_top_students(limit: int, db: Session = Depends(get_db)):
    students = db.query(models.Student)\
        .order_by(models.Student.marks.desc())\
        .limit(limit)\
        .all()
    return students