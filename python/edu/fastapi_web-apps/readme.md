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

documentation
```bash
http://0.0.0.0:8000/docs
http://0.0.0.0:8000/redoc
```

test url
```bash
curl http://0.0.0.0:8000/

curl http://0.0.0.0:8000/api/v1

curl -X "GET" http://0.0.0.0:8000/api/v1/notes \
  -H "accept: application/json"

curl -X "GET" http://0.0.0.0:8000/api/v1/notes/1 \
  -H "accept: application/json"

curl -X "POST" http://0.0.0.0:8000/api/v1/notes \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "data": "Example with text"}'

curl -X "PUT" http://0.0.0.0:8000/api/v1/notes/1 \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"data": "Updated data"}'

curl -X "DELETE" http://0.0.0.0:8000/api/v1/notes \
  -H "accept: application/json"

curl -X "DELETE" http://0.0.0.0:8000/api/v1/notes/1 \
  -H "accept: application/json"

```

-----

Helpers:

1. [Jinja filters](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters)
2. [Jinja inheritance](https://jinja.palletsprojects.com/en/3.0.x/templates/#template-inheritance)
3. --
