from fastapi import FastAPI
from pydantic import BaseModel

class TodoType(BaseModel):
    id:int
    task:str

TODO:list[TodoType]=[
    {"id":1,"task":"give me tha phone"}
]

app=FastAPI()

@app.get("/")
def root():
    return "hello World"

@app.get("/todo")
def todo():
    return TODO

@app.get("/todo/{id}")
def todo(id:int):
    for i in range(len(TODO)):
        if(id==TODO[i]["id"]):
            return TODO[i]
    return "no todo found"

@app.post("/todo")
def todo(todo:TodoType):
    for i in range(len(TODO)):
        if todo.id in TODO[i]["id"]:
            return "id already exist"
    TODO.append(todo)
    return todo

@app.delete("/todo/{id}")
def todo(id:int):
    for i in range(len(TODO)):
        if id == TODO[i]["id"]:
            TODO.pop(i)
            return "todo deleted..."
    return "id doesnt exist"

@app.put("/todo/{id}")
def todo(id:int,todo:TodoType):
    for i in range(len(TODO)):
        if id == TODO[i]["id"]:
            TODO[i]["task"] = todo.task        
            return todo
    return "id doesnt exist"



    
    



