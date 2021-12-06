from pydantic import BaseModel
from fastapi_users import models
from typing import Optional

# --- Collection Schema Setup -------------------------------------------
# Pydantic models for "Blog" + "User" collection schemas

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass

