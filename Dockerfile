FROM python:3.6

RUN apt-get update
#RUN apt-get update && apt-get install -y netcat gettext

RUN mkdir /code
RUN pip install --no-cache-dir pip -U
ADD requirements.txt /code
RUN pip install --no-cache-dir -r /code/requirements.txt

WORKDIR /app

#ADD entrypoint.sh /bin/entrypoint.sh

#RUN chmod +x /bin/entrypoint.sh
