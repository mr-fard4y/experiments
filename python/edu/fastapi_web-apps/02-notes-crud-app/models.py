from pydantic import BaseModel
from typing import List


class NoteItem(BaseModel):
    id: int
    data: str

    class Config:
        schema_extra = {"examples": [{"id": 1, "data": "Text data"}]}


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
