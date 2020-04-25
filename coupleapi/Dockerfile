FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /coupleapi
WORKDIR /coupleapi
COPY requirements.txt /coupleapi/
RUN pip install -r requirements.txt
COPY . /coupleapi/
