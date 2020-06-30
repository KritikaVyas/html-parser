FROM python:3.6.10-slim 
LABEL maintainer="Kritika Vyas"
ENV PYTHONUNBUFFERED  1
RUN apt-get update  

RUN mkdir /html-parser
WORKDIR /html-parser
ADD . /html-parser/

RUN pip install -r requirements.txt
CMD python3 src/htmlparser.py
