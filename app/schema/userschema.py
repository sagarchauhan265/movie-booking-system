from pydantic import BaseModel, Field, field_validator
import re

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
NAME_REGEX = r"^[a-zA-Z\s]+$"
PHONE_REGEX = r"^\d{10}$"


class UserBase(BaseModel):
    full_name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    phone: str =Field(...)

class UserRegister(UserBase):

    @field_validator("full_name")
    @classmethod
    def validate_name(cls, full_name: str) -> str:
        full_name = full_name.strip()
        if not full_name:
            raise ValueError("Name cannot be blank")
        if not re.match(NAME_REGEX, full_name):
            raise ValueError("Name must contain only letters and spaces")
        return full_name

    @field_validator("email")
    @classmethod
    def validate_email(cls, email: str) -> str:
        email = email.strip().lower()
        if not email:
            raise ValueError("Email cannot be blank")
        if not re.match(EMAIL_REGEX, email):
            raise ValueError("Invalid email format")
        return email

  

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if not password.strip():
            raise ValueError("Password cannot be blank")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError("Password must contain at least one special character")
        return password

    
    @field_validator("phone")
    @classmethod
    def validate_phone(cls, phone: str | None) -> str | None:
        if phone is None:
            return phone
        phone = phone.strip()
        if not re.match(PHONE_REGEX, phone):
            raise ValueError("Invalid phone number")
        return phone


class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    @field_validator("email")
    @classmethod
    def validate_email(cls, email: str) -> str:
        email = email.strip().lower()
        if not email:
            raise ValueError("Email cannot be blank")
        if not re.match(EMAIL_REGEX, email):
            raise ValueError("Invalid email format")
        return email

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if not password.strip():
            raise ValueError("Password cannot be blank")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError("Password must contain at least one special character")
        return password

    
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str | None
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True