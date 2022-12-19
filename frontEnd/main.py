from fastapi import FastAPI
import os, sys
import requests

app = FastAPI()

@app.get("/getFrom8080")
def get_root():
    x = requests.get('http://localhost:8080/test')
    return x.text
