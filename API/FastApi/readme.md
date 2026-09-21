# CloudTech Members API

A lightweight RESTful API built with **FastAPI** for managing organization members. It uses JSON file storage for persistent data management without requiring an external database setup.

---

##  Prerequisites & Installation

To run this application, make sure you have Python 3.8+ installed on your system. You will need to install **FastAPI**, **Pydantic**, and an ASGI server such as **Uvicorn**.

Required dependencies :

`` pip install fastapi uvicorn pydantic `` <br>
`` uvicorn main:cloudTechMembers --reload ``

## **Api Formate**
{
    "id": int,<br>
    "memberName": str,<br>
    "role": str<br>
}

## **Endpoints**
Get http://127.0.0.1:8000/Members <br>
Post http://127.0.0.1:8000/Members <br>
Put http://127.0.0.1:8000/Members/{member_id}
