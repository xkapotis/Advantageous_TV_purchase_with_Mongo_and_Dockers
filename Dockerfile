FROM python:3.6-buster

RUN pip install --upgrade pip 

ADD requirements.txt /Advantageous_TV_purchase_with_Mongo_and_Dockers/
WORKDIR /Advantageous_TV_purchase_with_Mongo_and_Dockers
RUN pip install -r requirements.txt
ADD  . /Advantageous_TV_purchase_with_Mongo_and_Dockers/

EXPOSE 8501