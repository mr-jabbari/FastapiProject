from fastapi import APIRouter


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/test")
def root():
    return {"message": "post routes is working"}

