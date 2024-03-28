from fastapi import HTTPException
from fastapi import FastAPI
from models import *
import uuid 
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Allow specified HTTP methods
    allow_headers=["*"],  # Allow requests with any headers
    allow_credentials=True,  # Allow credentials (cookies, authorization headers) to be sent
    expose_headers=["Content-Disposition"],  # Expose additional headers if needed
)
app.mount("/static", StaticFiles(directory="static"), name="static")

users = {"admin":{
  "username": "admin",
  "password": "pass@123",
  "email": "admin@admin.com"
}}

messages ={}


@app.get("/")
async def root():
   return FileResponse("static/index.html")

@app.get("/signup")
async def get_signup():
   return FileResponse("static/signup.html")

@app.get("/login")
async def get_login():
   return FileResponse("static/index.html")

@app.get("/dashboard")
async def get_dashboard():
   return FileResponse("static/dashboard.html")

@app.get("/getusers")
async def get_users():
   return {"message": users}




@app.post("/signup")
async def signup(user:Signup):
    if user.username in users:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    users[user.username] = {"username": user.username, "email": user.email, "password": user.password}
    raise HTTPException(status_code=200,detail="Registration Sucessfull")

'''
{
  "username": "admin",
  "password": "pass@123",
  "email": "admin@admin.com"
}
'''



@app.post("/login")
async def login(user:Login):
   if user.username in users:
    if users[user.username]["password"] == user.password:
        raise HTTPException(status_code=200,detail="logged in")
    else:
        raise HTTPException(status_code=400,detail="wrong username or password")
   else:
      raise HTTPException(status_code=400,detail="wrong username or password")
   
'''
{
  "username": "admin",
  "password": "pass@123"
}
'''

      
@app.post("/forgot")   
async def forget_pass(request:Forgot):
   if request.new_pass == request.repeat_pass:
      if request.username in users:
         if users[request.username]["password"] == request.old_pass:
            users[request.username]["password"] = request.new_pass
            raise HTTPException(status_code=200,detail="Password Updated")
         raise HTTPException(status_code=400,detail="wrong username or password")
      raise HTTPException(status_code=400,detail="wrong username or password")
   raise HTTPException(status_code=400,detail="new password and repeat password does not match")
         
'''
{
  "username": "admin",
  "old_pass": "pass@123",
  "new_pass": "string",
  "repeat_pass": "string"
}
'''

@app.post("/message")
async def post_message(message: Message):
    if message.username in users:
       u = uuid.uuid1()
       t = datetime.now()
       messages[str(u)] = {"username": message.username, "message": message.text,"time":t}
       return messages
    raise HTTPException(status_code=400,detail="invalid")


'''
{
  "username": "admin",
  "text": "string"
}
'''

@app.get("/message")
async def message():
   return messages

@app.get("/getmessage")
async def get_message(message:GetMessage):
   if message.username in users:
      for m in messages:
        pass

      text = messages[message.message_id]["message"]
      return {"message":text}
   raise HTTPException(status_code=400,detail="invalid")


@app.options("/{path:path}")
async def options_handler(request: Request, path: str):
    return {"message": "Allow: GET, POST, PUT, DELETE, OPTIONS"} 