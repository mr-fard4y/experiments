from pydantic import BaseModel


class NoteItem(BaseModel):
    id: int
    data: str

    class Config:
        schema_extra = {"examples": [{"id": 1, "data": "Text data"}]}


class NoteItemUpdate(BaseModel):
    data: str

    class Config:
        schema_extra = {"examples": [{"data": "Updated text data"}]}
