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
# uvicorn <module-name>:<app-name> --port <port> --reload
# uvicorn api:app --port 8000 --reload

uvicorn notes-api:app --port 8000 --reload
```

test url
```bash
curl http://0.0.0.0:8000/

curl http://0.0.0.0:8000/api/v1

curl -X "GET" http://0.0.0.0:8000/api/v1/items \
  -H "accept: application/json"

curl -X "POST" http://0.0.0.0:8000/api/v1/items \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "data": "Example with text"}'

```
