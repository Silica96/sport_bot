FROM python:3.10-alpine
RUN mkdir /data
COPY requirements.txt /data
COPY python/ /data
WORKDIR /data
RUN pip install -r requirements.txt

CMD [ "python3", "telegram_bot.py" ]