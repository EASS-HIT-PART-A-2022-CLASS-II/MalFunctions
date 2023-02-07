from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
from models import MalFunction
import json




app = FastAPI()

origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

malfunctions  = []

#####all http requests below will call MalFunction Service#####

#http request to get entire malfunctions list
@app.get("/check")
def check():
    r = requests.get("http://database_service/check")
    return r.json()

@app.get("/getList")
def getList():
    r = requests.get("http://database_service/getList")
    return r.json()
    
@app.post("/addMal")
def addMal(mal: MalFunction):
    mal.date = str(mal.date)
    ss = json.dumps(mal.dict())
    r = requests.post("http://database_service/addMal", data=ss)
    return r.json()

@app.delete("/delMal/{id}")
def delMal(id : int):
    r = requests.delete("http://database_service/delMal/" + str(id))
    return r.json()

@app.post("/editMal")
def editMal(mal: MalFunction):
    mal.date = str(mal.date)
    ss = json.dumps(mal.dict())
    r = requests.post("http://database_service/editMal", data=ss)
    return r.json()

