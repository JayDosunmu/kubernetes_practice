FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /config
COPY ./requirements.txt /config
WORKDIR /config
RUN pip install -r requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./ .

CMD ["python", "api.py"]