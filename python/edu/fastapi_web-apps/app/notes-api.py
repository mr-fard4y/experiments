from fastapi import FastAPI, APIRouter


DATABASE: list[dict] = []


router = APIRouter(prefix="/api/v1")


@router.get("/")
async def get_version() -> dict:
    return {"version": "v1"}


@router.get("/items")
async def get_all_data() -> dict:
    return {"data": DATABASE}


@router.post("/items")
async def create_item(item: dict) -> dict:
    DATABASE.append(item)
    return {"result": "Item has added successfully"}


app = FastAPI()
app.include_router(router)


@app.get("/")
async def health_check() -> dict:
    return {"status": "OK"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("notes-api:app", host="127.0.0.1", port=8000, reload=True)
