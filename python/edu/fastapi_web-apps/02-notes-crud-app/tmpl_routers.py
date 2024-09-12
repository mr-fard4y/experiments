from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from models import NoteItem

from routers import DATABASE


tmpl_router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@tmpl_router.get("/notes")
async def get_all_data_tmpl(request: Request):
    response = {"request": request, "items": DATABASE}
    return templates.TemplateResponse("notes.html", response)


@tmpl_router.post("/notes", status_code=status.HTTP_201_CREATED)
async def create_item(
        request: Request,
        item: NoteItem = Depends(NoteItem.as_form)
):
    item.id = len(DATABASE) + 1
    DATABASE.append(item)
    response = {"request": request, "items": DATABASE}
    return templates.TemplateResponse("notes.html", response)


@tmpl_router.get("/notes/{item_id}")
async def retrieve_item(
        request: Request,
        item_id: int = Path(..., title="Item ID")
):
    for item in DATABASE:
        if item.id == item_id:
            response = {"request": request, "item_info": item}
            return templates.TemplateResponse("notes.html", response)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Item doesn't exist"
    )
