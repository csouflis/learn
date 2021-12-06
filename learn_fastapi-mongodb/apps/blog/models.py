from typing import Optional
import uuid
from pydantic import BaseModel, Field


class BlogModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    body: str = Field(...)
    published: bool = False

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "title": "My crazy blogpost",
                "body": "Lorem ipsum topsy turfy Wurtle the turtle is great. How weird it is to write random words.",
                "published": False,
            }
        }


class UpdateBlogModel(BaseModel):
    name: Optional[str]
    completed: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "title": "My crazy blogpost",
                "body": "Lorem ipsum topsy turfy Wurtle the turtle is great. How weird it is to write random words.",
                "published": False,
            }
        }
