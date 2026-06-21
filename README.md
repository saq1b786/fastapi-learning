# FastAPI Players API

A REST API for managing football players, built with FastAPI and SQLite. My first API project — learning how to build backend services with proper endpoints and database persistence.

## Features

- Add players via POST request with automatic validation
- Retrieve all players or search by name
- Delete players from the database
- Persistent SQLite storage — data survives server restarts
- Auto-generated interactive API documentation at /docs

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then visit http://localhost:8000/docs to interact with the API.

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | /players | Get all players |
| POST | /players | Add a new player |
| GET | /players/{name} | Get a single player |
| DELETE | /players/{name} | Delete a player |

## Project Structure

fastapi-learning/

main.py        — API endpoints

models.py      — Pydantic data models

database.py    — SQLite database operations

players.db     — Auto-generated database

## Built With

- Python 3
- FastAPI
- SQLite3
- Pydantic for data validation

## What I Learned

- Building REST APIs with FastAPI
- HTTP methods: GET, POST, DELETE
- Pydantic BaseModel for request validation
- Connecting an API to a SQLite database
- Separating concerns: models, database, and routes
- Auto-generated API documentation with Swagger UI