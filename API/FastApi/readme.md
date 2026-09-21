# CloudTech Members API

A lightweight RESTful API built with **FastAPI** for managing organization members. It uses JSON file storage for persistent data management without requiring an external database setup.

---

## Prerequisites & Installation

To run this application, make sure you have Python 3.8+ installed on your system. You will need to install **FastAPI**, **Pydantic**, and an ASGI server such as **Uvicorn**.

Required dependencies:

```bash
pip install fastapi uvicorn pydantic
uvicorn main:cloudTechMembers --reload
```

## **API Format**

```json
{
    "id": int,
    "memberName": str,
    "role": str
}
```

## **Authentication**

The `/auth` endpoint is used to generate an authentication token.

**POST** `http://127.0.0.1:8000/auth`

Request body:

```json
{
    "username": "",
    "password": ""
}
```

Response:

```json
{
    "access_token": "generated_token"
}
```

The returned `access_token` must be provided in the **header** when creating a new member.

Header:

```text
token: generated_token
```

## **Endpoints**

**GET** `http://127.0.0.1:8000/Members`

**POST** `http://127.0.0.1:8000/Members`
Requires authentication token in the header.

**PUT** `http://127.0.0.1:8000/Members/{member_id}`

**PATCH** `http://127.0.0.1:8000/Members/{member_id}`

**DELETE** `http://127.0.0.1:8000/Members/{member_id}`

**GET** `http://127.0.0.1:8000/Members/{member_id}`
