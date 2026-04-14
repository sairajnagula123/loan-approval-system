# app/auth_utils.py
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from .. import models, database

import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_current_user(token: str = Depends(lambda: None), db: Session = Depends(database.get_db)):
    """
    This function is a simplified dependency. Instead of retrieving token from header in this lambda default,
    in FastAPI you should use OAuth2PasswordBearer or a custom dependency.
    For practical usage, import OAuth2PasswordBearer and decode Authorization header.
    We'll implement a simple header extraction dependency in login route usage below.
    """
    raise HTTPException(status_code=501, detail="Use the provided get_current_user_from_header in routes")

# Provide a more usable dependency that pulls token from Authorization header
from fastapi import Header, Request

def get_current_user_from_header(authorization: str | None = Header(default=None), db: Session = Depends(database.get_db)):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing")
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth scheme")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if not email:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
