from fastapi import FastAPI
from routers import router


app = FastAPI()
app.include_router(router)


@app.get("/")
async def health_check() -> dict:
    return {"status": "OK"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("notes-api:app", host="127.0.0.1", port=8000, reload=True)
