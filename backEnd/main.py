from fastapi import FastAPI
from models import *
import os, sys
app = FastAPI()

firstMalFunction = MalFunctionDto(id=1,date="20/12/22",description="fix toilet",status="completed")
secondMalFunction = MalFunctionDto(id=2,date="22/12/22",description="fix main door", status="in progress")

malfunctions  = [firstMalFunction,secondMalFunction]


@app.get("/test")
def hello_post():
    return "test works!"

@app.get("/getMalList")
def getMalfuntionList():
    return {"MalFunctions list":malfunctions,"meta_data":len(malfunctions)}






#####all http requests below will call MalFunction Service#####

#http request to get entire malfunctions list
@app.get("/getMalFunctionsList")
def getMalfuntionList():
    return print("call malfunction service and get back list of all malfunctions")


#http request to remove specific malfunction by id
@app.post("/removeMalFunction")
def removeMalFunction(id:int):
    return print("send id for remove from DB by malfunction service")


#http request to update specific malfunction object with specific id will send and change in DB
@app.post("/updateMalFunction")
def updateMalFunction(updatedMalFunction: MalFunctionDto):
    return print("send updated malfunction to malfunction service for update")


#http request to add new malfunction to DB
@app.post("/addMalFunction")
def addMalFunction(newMalFunction: MalFunctionDto):
    return print("send new dto for register in DB")

