from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)


@app.get("/")
async def root():
    return {"message": "FastAPI is working"}
