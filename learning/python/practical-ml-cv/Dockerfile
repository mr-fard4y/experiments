FROM python:3.8-slim

WORKDIR /opt/app

COPY . .

RUN pip3 install --upgrade pip \
   && pip3 install -r requirements.txt

ENTRYPOINT ["jupyter", "notebook", "--ip", "0.0.0.0", "--allow-root"]
