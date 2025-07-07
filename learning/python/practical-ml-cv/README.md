

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

-----
### 

step - 1

```bash

# python 01-classification/class-activation-map.py --process image --path examples/dog.png

ffmpeg -i examples/video-input.mov -vf fps=25 examples/video-picts/thumb%04d.jpg -hide_banner
python 01-classification/class-activation-map.py --process video --path examples/video-picts/
ffmpeg -framerate 25 -i examples/video-class-map/result-%04d.jpg video-output.mp4
```