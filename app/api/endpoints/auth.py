from fastapi import APIRouter, Form, Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.services.auth_service import  auth_login_service, auth_user_register_service
from app.schema.userschema import UserCreate, UserLogin, UserRegister
from app.config.db import SessionLocal, get_db

auth_router = APIRouter()




@auth_router.post("/signup")
async def auth_signup(
        full_name: str = Form(...),
        email :str = Form(...),
        password: str = Form(...),
        phone: str = Form(...),
        db:Session = Depends(get_db)
        ):
         try:
            data = UserRegister(email=email, password=password, full_name=full_name, phone=phone)
         except ValidationError as e:
            errors = [{"field": err["loc"][0], "message": err["msg"]} for err in e.errors()]
            raise HTTPException(status_code=422, detail=errors)
         return  auth_user_register_service(data,db) 
       

        

       







# @auth_router.post("/signup")
# def auth_signup(
#     q:str,
#     name:str = Form(...),
#     # email:str = Form(...),
#     # image:File = File(...),
#     ):

#     return {
#         "status":"ok signup",
#         "name":name,
#         "search":q

#     }

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
    return auth_login_service(data.email, data.password, db)