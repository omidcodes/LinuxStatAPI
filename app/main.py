from fastapi import FastAPI
from app.api.v1.endpoints import user

app = FastAPI(title="My FastAPI App")

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])