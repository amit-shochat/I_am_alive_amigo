# base image 
FROM python:3.8-slim-buster

# ENV 
ENV SLEEP_SECONDS="5"
ENV RUN_SECONDS="300" 
ENV RUN_FOR_EVER="no" 

# Working DIR 
WORKDIR /python-app

COPY . .

# Run Flask web server 
CMD [ "python3", "I_am_alive_5Sec.py"]
