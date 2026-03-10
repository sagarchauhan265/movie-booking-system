from app.models.user import User
from fastapi import HTTPException
import re
from app.utils.utils import _hash_password, _verify_password


# def _hash_password(password: str) -> str:
#     return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# def _verify_password(password: str, hashed: str) -> bool:
#     return bcrypt.checkpw(password.encode(), hashed.encode())


def auth_login_service(email: str, password: str, db):

    db_user = db.query(User).filter(User.email == email.strip()).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not _verify_password(password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "status": "success",
        "data": db_user
    }


def auth_user_register_service(user, db):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise ValueError("EMAIL_ALREADY_EXISTS")
    hashed_password = _hash_password(user.password)
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hashed_password,
        phone=user.phone
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "status": "success",
        "data": new_user
    }