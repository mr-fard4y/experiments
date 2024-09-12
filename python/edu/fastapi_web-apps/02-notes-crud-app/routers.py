from fastapi import APIRouter, Path, HTTPException, status
from models import NoteItem, NoteItemUpdate, NoteItemsResponse


DATABASE: list[NoteItem] = []


router = APIRouter(prefix="/api/v1")


@router.get("/")
async def get_version() -> dict:
    return {"version": "v1"}


@router.get("/notes", response_model=NoteItemsResponse)
async def get_all_data() -> dict:
    return {"data": DATABASE}


@router.get("/notes/{item_id}")
async def retrieve_item(item_id: int = Path(..., title="Item ID")) -> dict:
    for item in DATABASE:
        if item.id == item_id:
            return {"data": item}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Item doesn't exist"
    )


@router.post("/notes", status_code=status.HTTP_201_CREATED)
async def create_item(item: NoteItem) -> dict:
    DATABASE.append(item)
    return {"result": "Item has added successfully"}


@router.put("/notes/{item_id}")
async def update_item(
    item_data: NoteItemUpdate, item_id: int = Path(..., title="Item ID")
) -> dict:
    for item in DATABASE:
        if item.id == item_id:
            item.data = item_data.data
            return {"result": "Item has updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Item doesn't exist"
    )


@router.delete("/notes")
async def clear_db() -> dict:
    DATABASE.clear()
    return {"result": "All items have removed successfully"}


@router.delete("/notes/{item_id}")
async def remove_item(item_id: int) -> dict:
    for idx, item in enumerate(DATABASE):
        if item.id == item_id:
            DATABASE.pop(idx)
            return {"result": "Item has removed successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Item doesn't exist"
    )
