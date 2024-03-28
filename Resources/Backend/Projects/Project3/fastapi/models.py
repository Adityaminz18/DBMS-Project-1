from pydantic import BaseModel,BeforeValidator,EmailStr
from typing import Dict, Any


class User(BaseModel):
    uid: int
    username: str

class Login(BaseModel):
    username: str
    password: str

class Signup(BaseModel):
    username: str
    password: str
    email: EmailStr

class Forgot(BaseModel):
    username: str
    old_pass:str
    new_pass:str
    repeat_pass:str

class Message(BaseModel):
    username:str
    text:str

class GetMessage(BaseModel):
    message_id:str

class Request(BaseModel):
    app: Any
    method: str
    url: str
    headers: Dict[str, str]
    query_params: Dict[str, str]
    path_params: Dict[str, Any]
    cookies: Dict[str, str]
    state: Dict[str, Any]
    session: Dict[str, Any]
    files: Dict[str, Any]