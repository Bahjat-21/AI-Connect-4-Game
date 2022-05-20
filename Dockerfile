FROM python:3.10-alpine 

ADD connect4.py .

CMD [ "python", "./connect4.py" ]