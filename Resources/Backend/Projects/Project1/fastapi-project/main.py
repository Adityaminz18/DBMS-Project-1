from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

## Get all Todos
@app.get("/todos")
async def get_todos():
    return {"todo": todos}

## get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo":todo}
    return {"todo":"No todos found"}


## Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message":"todo has been added"}
    

## update todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int,todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.item = todo_obj.item
            return {"todo":"todo updated"}
    return {"todo":"No todos found"}

## delete todo
@app.delete("/todos/{todo_obj}")
async def delete_todos(todo_obj: int):
    for todo in todos:
        if todo.id == todo_obj:
            todos.remove(todo)
            return {"todo":"todo has been deleted"}
    return {"todo":"No todos found"}