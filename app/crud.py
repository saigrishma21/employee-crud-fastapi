from sqlalchemy.orm import Session

from .models import Employee
from .schemas import EmployeeCreate, EmployeeUpdate


def create_employee(
    db: Session,
    employee: EmployeeCreate
):
    db_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        designation=employee.designation,
        salary=employee.salary
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def get_employees(db: Session):
    return db.query(Employee).all()


def get_employee(
    db: Session,
    employee_id: int
):
    return (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )


def update_employee(
    db: Session,
    employee_id: int,
    employee: EmployeeUpdate
):
    db_employee = get_employee(db, employee_id)

    if not db_employee:
        return None

    update_data = employee.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)

    return db_employee


def delete_employee(
    db: Session,
    employee_id: int
):
    db_employee = get_employee(db, employee_id)

    if not db_employee:
        return None

    db.delete(db_employee)
    db.commit()

    return db_employee