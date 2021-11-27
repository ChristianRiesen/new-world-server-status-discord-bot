FROM python:3

ADD main.py /
ADD config.py /
ADD worldupdate.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "-u", "./main.py" ]
