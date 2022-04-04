from email import header
import json
from django.conf import settings
from django.forms import ValidationError
import requests
from getpass import getpass
from rest_framework.response import Response
import jwt
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY') #Import Your project key, because jwt uses it to hash the tokens so you will need it to decode the token to get your user 
info = {
    "email": "aka@gmail.com",
    "password": "aka"
}
getToken = requests.post("http://127.0.0.1:8000/token/",json=info)
token =(getToken.json()['access'])
decode= jwt.decode(token, SECRET_KEY, algorithms=['HS256',] ) #Project secret key used here for decoding 
user_id = decode['user_id']
data = {
    "token":f"{token}"
}
verifyToken = requests.post("http://127.0.0.1:8000/token/verify/",json=data)
headers = {
    "content-type":"application/json",
    "Authorization":f"Bearer {token}", #Users jwt useed for creating  a post 
}
data= {
    "size": "MEDIUM",
    "quantity": 190000
}
#     print("access granted")
createOrder = requests.post(f"http://127.0.0.1:8000/orders/user/{user_id}/create/",json=data, headers=headers)

       
  
        
