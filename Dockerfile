FROM python:3.8

WORKDIR /usr/src

COPY requirements.txt /usr/src

RUN pip install -r requirements.txt

COPY . /usr/src

CMD ["python", "./south-park-random.py"]