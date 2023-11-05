from fastapi.middleware.cors import CORSMiddleware
from .routers import routes_post, routes_user
from fastapi import FastAPI


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_post.router)
app.include_router(routes_user.router)


@app.get("/")
async def root():
    return {"message": "FastAPIApp is working!!"}
