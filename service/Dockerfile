FROM python:3.10.0-alpine3.14
MAINTAINER JCUEVAS <JOSE.CUEVAS.CV@GMAIL.COM>
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip 
 
COPY . /code/
RUN pip install -r requirements.txt

WORKDIR /code/main
EXPOSE 8000
ENTRYPOINT [ "python" ]

CMD [ "src" ]