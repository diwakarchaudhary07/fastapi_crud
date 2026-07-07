from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():

    return {"message": "FastAPI CRUD Running"}


@app.post("/students/")
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)


@app.get("/students/")
def read_students(
    db: Session = Depends(get_db)
):
    return crud.get_students(db)


@app.get("/students/{student_id}")
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_student(db, student_id)


@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_student(db, student_id)