FROM python:3.7.9-buster
MAINTAINER JCUEVAS <JOSE.CUEVAS.CV@GMAIL.COM>
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip

RUN apt-get update
COPY Pantallas /code/
RUN bash /code/install.sh
RUN pip install -r requirements.txt
COPY . /code/
WORKDIR /code/main
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
