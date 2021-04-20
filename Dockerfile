FROM python:3.8.5
MAINTAINER mami.mokhtar123@gmail.com
COPY ./ /PWB
WORKDIR /PWB/pwb
RUN pip install -r  /PWB/full_requirements.txt
EXPOSE 80