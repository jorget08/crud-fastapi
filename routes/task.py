from fastapi import APIRouter, Depends
from config.db import conn
from models.task import tasks
from schemas.task import Task, UpdateTask
from auth.auth import AuthHandler


task = APIRouter()
auth_handler = AuthHandler()


@task.get('/tasks')
def list_tasks(email=Depends(auth_handler.auth_wrapper)):
    return conn.execute(tasks.select()).fetchall()

@task.post('/tasks')
def create_task(task:Task, email=Depends(auth_handler.auth_wrapper)):
    new_task = {"name": task.name, "description": task.description, "date": task.date}
    print(task)
    result = conn.execute(tasks.insert().values(new_task))
    return conn.execute(tasks.select().where(tasks.c.id == result.lastrowid)).first()

@task.get('/tasks/{id}')
def list_a_task(id:str, email=Depends(auth_handler.auth_wrapper)):
    return conn.execute(tasks.select().where(tasks.c.id == id)).first()

@task.put('/tasks/{id}')
def update_task(task:UpdateTask, id: str, email=Depends(auth_handler.auth_wrapper)):
    #conn.execute(tasks.update().values(name=task.name, description=task.description, date=task.date).where(tasks.c.id == id))
    if task.name:
        conn.execute(tasks.update().values(name=task.name).where(tasks.c.id == id))
    if task.description:
        conn.execute(tasks.update().values(description=task.description).where(tasks.c.id == id))
    if task.date:
        conn.execute(tasks.update().values(date=task.date).where(tasks.c.id == id))
    return "Task updated successfully"

@task.delete('/tasks/{id}')
def delete_task(id: str, email=Depends(auth_handler.auth_wrapper)):
    conn.execute(tasks.delete().where(tasks.c.id == id))
    return "Deleted"