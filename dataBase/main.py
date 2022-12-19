import mysql.connector
from fastapi import FastAPI
app = FastAPI()

@app.get("/test")
def printtext():
    mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            password="1542")
    return mydb


