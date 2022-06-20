
FROM python:3.10-slim-bullseye 
WORKDIR /usr/src

RUN pip install --upgrade pip

#COPY src/requirements.txt /usr/src/
#RUN pip install --user -r /usr/src/requirements.txt

RUN pip install numpy==1.22.1

COPY src/connect4.py /usr/src/

CMD [ "python", "/usr/src/connect4.py"]