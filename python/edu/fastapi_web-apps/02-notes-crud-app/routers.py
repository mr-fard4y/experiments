from fastapi import APIRouter, Path
from models import NoteItem, NoteItemUpdate


DATABASE: list[NoteItem] = []


router = APIRouter(prefix="/api/v1")


@router.get("/")
async def get_version() -> dict:
    return {"version": "v1"}


@router.get("/items")
async def get_all_data() -> dict:
    return {"data": DATABASE}


@router.get("/items/{item_id}")
async def retrieve_item(item_id: int = Path(..., title="Item ID")) -> dict:
    for item in DATABASE:
        if item.id == item_id:
            return {"data": item}
    return {"result": "Item doesn't exist"}


@router.post("/items")
async def create_item(item: NoteItem) -> dict:
    DATABASE.append(item)
    return {"result": "Item has added successfully"}


@router.put("/items/{item_id}")
async def update_item(
    item_data: NoteItemUpdate, item_id: int = Path(..., title="Item ID")
) -> dict:
    for item in DATABASE:
        if item.id == item_id:
            item.data = item_data.data
            return {"result": "Item has updated successfully"}
    return {"result": "Item doesn't exist"}


@router.delete("/items")
async def clear_db() -> dict:
    DATABASE.clear()
    return {"result": "All items have removed successfully"}


@router.delete("/items/{item_id}")
async def remove_item(item_id: int) -> dict:
    for idx, item in enumerate(DATABASE):
        if item.id == item_id:
            DATABASE.pop(idx)
            return {"result": "Item has removed successfully"}
    return {"result": "Item doesn't exist"}
