# Employee CRUD API

A RESTful Employee Management API built using **FastAPI, PostgreSQL, SQLAlchemy, and Pydantic**. The application provides complete CRUD operations for managing employee records and can be tested using Swagger UI and Postman.

## Features

- Create employees
- View all employees
- View employee by ID
- Update employee details
- Delete employees
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic data validation
- RESTful API architecture
- Swagger/OpenAPI documentation
- Postman API testing
- Environment variable configuration

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- Psycopg2
- Python-dotenv
- Swagger UI
- Postman

## Project Structure

```text
employee-crud-fastapi/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   └── routers/
│       ├── __init__.py
│       └── employees.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
