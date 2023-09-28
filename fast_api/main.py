import json
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import Constant

class User(BaseModel):
    Name:str
    Email:str
    Phone:str
    Address:str

class Field(BaseModel):
    fields : User

app = FastAPI()

URL = "https://api.airtable.com/v0/"+Constant.BaseID+"/"+Constant.TableName
headers = {"Authorization": "Bearer "+Constant.TOKEN,
           "Content-Type": "application/json"}

@app.get("/")
def get_all_data():
    response=requests.get(URL,headers=headers)
    return response.json()


@app.get("/user/{user_id}/")
def get_user(user_id: str):
    response = requests.get(URL+"/"+user_id,headers=headers)
    return response.json()

@app.post("/adduser/")
def add_user(fields:Field):
    fields = fields.model_dump()
    respose=requests.post(URL,data=json.dumps(fields),headers=headers)
    return respose.json()

@app.patch("/user/{user_id}/")
def update_user(user_id: str, fields:Field):
    fields = fields.model_dump()
    response = requests.patch(URL+"/"+user_id,data=json.dumps(fields),headers=headers)
    return response.json()

@app.patch("/user/{user_id}/")
def delete_user(user_id: str):
    response = requests.delete(URL+"/"+user_id,headers=headers)
    return response.json()
