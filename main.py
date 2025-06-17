from fastapi import FastAPI
from pydantic import BaseModel

class TodoType(BaseModel):
    id:int
    task:str

TODO:list=[]

app=FastAPI()

@app.get("/")
def root():
    return "hello World"
