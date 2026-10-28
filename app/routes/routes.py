import sys
import models


from bson import ObjectId
from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from app.models.todo import TodoModel
from dependencies import get_db
from pymongo.database import Database
from pymongo import ReturnDocument 


bp = APIRouter(prefix="/api", tags=["todos"], responses={404: {"description": "Not found"}})

models.Base.metadata.create_all(bind=models.engine)


def get_db(): 
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@bp.get("/", response_class=HTMLResponse)


@bp.get("/todos/stats", response_model=List[TodoModel])
async def get_todos(db: Database = Depends(get_db)):
    tasks = repo().list()
    total = len(tasks)
    done = sum(1 for task in tasks if task.done)
    return jsonify({"total": total, "done": done, "tasks": tasks})


