from fastapi import APIRouter


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/")
def root():
    return {"message": "this is posts"}
