from fastapi import APIRouter, Form, Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.services.auth_service import  auth_login_service, auth_user_register_service
from app.schema.userschema import UserLogin, UserRegister
from app.config.db import SessionLocal, get_db

auth_router = APIRouter()

@auth_router.post("/signup")
async def auth_signup(
    full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    phone: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
       user = UserRegister(full_name=full_name, email=email, password=password,phone=phone)   
    except ValidationError as e:
        errors = [{"field": err["loc"][0], "message": err["msg"]} for err in e.errors()]
        raise HTTPException(status_code=422, detail=errors)
    result = auth_user_register_service(user, db)
    return result


@auth_router.post("/login")
def auth_login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        data = UserLogin(email=email, password=password)
    except ValidationError as e:
        errors = [{"field": err["loc"][0], "message": err["msg"]} for err in e.errors()]
        raise HTTPException(status_code=422, detail=errors)
    return auth_login_service(data, db)