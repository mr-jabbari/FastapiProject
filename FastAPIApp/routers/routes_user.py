from fastapi import APIRouter
from fastapi import HTTPException, Body
from fastapi.encoders import jsonable_encoder
from FastAPIApp.database import db
from FastAPIApp.functions import student_helper
from FastAPIApp.schemas import StudentSchema, ResponseModel, UpdateStudentModel


router = APIRouter(
    prefix="/users",
    tags=['Users'])


@router.get("/test")
def root():
    return {"message": "user routes is working"}


@router.post("/", response_description="Add new student", response_model=StudentSchema)
async def create_student(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await db["students"].insert_one(student)
    created_student = await db["students"].find_one({"_id": new_student.inserted_id})
    return ResponseModel(student_helper(created_student), "Student added successfully.")


@router.get("/", response_description="List all students", response_model=ResponseModel)
async def list_students():
    students = await db["students"].find().to_list(1000)
    if students:
        return ResponseModel(items=[student_helper(student) for student in students],
                             message="Students data retrieved successfully")
    return ResponseModel(items=[], message="Empty list returned")


@router.get("/{id}", response_description="Get a single student", response_model=StudentSchema)
async def show_student(id: str):
    if (student := await db["students"].find_one({"_id": id})) is not None:
        return ResponseModel(student_helper(student), "Student data retrieved successfully")
    raise HTTPException(status_code=404, detail=f"Student with ID {id} doesn't exist")


@router.put("/{id}", response_description="Update a student", response_model=StudentSchema)
async def update_student(id: str, student: UpdateStudentModel = Body(...)):
    student = {k: v for k, v in student.model_dump().items() if v is not None}
    if len(student) >= 1:
        update_result = await db["students"].update_one({"_id": id}, {"$set": student})
        if update_result.modified_count == 1:
            if (updated_student := await db["students"].find_one({"_id": id})) is not None:
                return ResponseModel(student_helper(updated_student), "Student updated successfully")
    if (existing_student := await db["students"].find_one({"_id": id})) is not None:
        return ResponseModel(student_helper(existing_student), "Nothing to update")
    raise HTTPException(status_code=404, detail=f"Student with ID {id} doesn't exist")


@router.delete("/{id}", response_description="Delete a student", response_model=StudentSchema)
async def delete_student(id: str):
    delete_result = await db["students"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return ResponseModel({"id": id}, "Student deleted successfully")
    raise HTTPException(status_code=404, detail=f"Student with ID {id} doesn't exist")
