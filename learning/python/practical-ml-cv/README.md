

###
Environment

Jupyter
```bash
# installation

pip intall notebook

# or (alternative)
pip3 install -r requirements.txt
```

```bash
# running

jupyter notebook
```

Docker
```bash
# build

docker build -t ml-cv/base:0.0 .

# run for testing
# docker run -it --rm ml-cv/base:0.0 "bash"

docker run --rm -p 8888:8888 -v .:/opt/app ml-cv/base:0.0
docker exec -it <container-id> bash
```
