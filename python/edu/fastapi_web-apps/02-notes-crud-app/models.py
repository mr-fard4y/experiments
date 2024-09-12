from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional


class NoteItem(BaseModel):
    id: Optional[int]
    data: str

    class Config:
        schema_extra = {"examples": [{"id": 1, "data": "Text data"}]}

    @classmethod
    def as_form(cls, description: str = Form(...)):
        return cls(data=description)


class NoteItemUpdate(BaseModel):
    data: str

    class Config:
        schema_extra = {"examples": [{"data": "Updated text data"}]}


class NoteItemResponse(BaseModel):
    data: str

    class Config:
        schema_extra = {"examples": [{"data": "Text information"}]}


class NoteItemsResponse(BaseModel):
    data: List[NoteItemResponse]

    class Config:
        schema_extra = {
            "examples": [
                {"data": [{"data": "Example 1"}, {"data": "Example 2"}]}
            ]
        }
