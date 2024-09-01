FastAPI. Web-app projects

-----

Docker

```bash

docker build -t fast-api-test .
# docker build -t fast-api-test ch1/Dockerfile

docker run fast-api-test
```

-----

FastAPI

Installation

```bash
pip install fastapi
pip install uvicorn
```

start app
```bash
uvicorn api:app --port 8000 --reload
```

test url
```bash
curl http://0.0.0.0:8000/
```
