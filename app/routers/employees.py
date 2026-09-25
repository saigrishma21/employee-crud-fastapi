from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..crud import (
    create_employee,
    delete_employee,
    get_employee,
    get_employees,
    update_employee
)
from ..database import get_db
from ..schemas import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    existing_employee = (
        db.query(__import__(
            "app.models",
            fromlist=["Employee"]
        ).Employee)
        .filter(
            __import__(
                "app.models",
                fromlist=["Employee"]
            ).Employee.email == employee.email
        )
        .first()
    )

    if existing_employee:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    try:
        return create_employee(db, employee)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Employee could not be created"
        )


@router.get(
    "/",
    response_model=list[EmployeeResponse]
)
def read_all(
    db: Session = Depends(get_db)
):
    return get_employees(db)


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def read_one(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = get_employee(db, employee_id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    existing_employee = get_employee(
        db,
        employee_id
    )

    if not existing_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    if employee.email:
        email_employee = (
            db.query(
                __import__(
                    "app.models",
                    fromlist=["Employee"]
                ).Employee
            )
            .filter(
                __import__(
                    "app.models",
                    fromlist=["Employee"]
                ).Employee.email == employee.email
            )
            .first()
        )

        if (
            email_employee
            and email_employee.id != employee_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

    try:
        return update_employee(
            db,
            employee_id,
            employee
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Employee could not be updated"
        )


@router.delete(
    "/{employee_id}"
)
def delete(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = delete_employee(
        db,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee_id": employee_id
    }