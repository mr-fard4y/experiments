from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import router
from tmpl_routers import tmpl_router


app = FastAPI()
app.include_router(router)
app.include_router(tmpl_router)


@app.get("/status")
async def health_check() -> dict:
    return {"status": "OK"}


@app.get("/")
async def inbox():
    return RedirectResponse("/notes")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("notes-api:app", host="127.0.0.1", port=8000, reload=True)
