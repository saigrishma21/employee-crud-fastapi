from fastapi import FastAPI

from .database import Base, engine
from .routers.employees import router as employee_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    description="FastAPI CRUD API for Employee Management",
    version="1.0.0"
)

app.include_router(employee_router)


@app.get("/")
def root():
    return {
        "message": "Employee Management API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }