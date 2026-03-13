from passlib.context import CryptContext
from fastapi import HTTPException

def  PassWord_Verify(user_password, db_user_password):

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    if not pwd_context.verify(user_password, db_user_password):
         raise HTTPException(status_code=400, detail="Incorrect password")
    

    return True
