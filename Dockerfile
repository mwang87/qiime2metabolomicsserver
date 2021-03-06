FROM qiime2/core:2019.1
MAINTAINER Mingxun Wang "mwang87@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN pip install urllib3==1.23
RUN pip install peewee
RUN pip install flask
RUN pip install requests
RUN pip install requests-cache
RUN pip install gunicorn
RUN pip install xmltodict
RUN apt-get install -y unzip
RUN pip install git+https://github.com/mwang87/q2_metabolomics.git@2

RUN pip install metabodisttrees
RUN pip install obonet

COPY . /app
WORKDIR /app
