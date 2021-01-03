FROM ubuntu:18.04

RUN apt update -y && apt -y install wget git python3.6 python3-pip tar

RUN pip3 install Flask

RUN pip3 install beautifulsoup4

RUN pip3 install requests

RUN mkdir flask_test

RUN cd /flask_test/ && git clone https://github.com/jung211p/inspien.git

CMD cd /flask_test/inspien && python3 /flask_test/inspien/corona.py
