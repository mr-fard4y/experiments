from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello() -> dict:
    return {"data": "Hello friend"}
