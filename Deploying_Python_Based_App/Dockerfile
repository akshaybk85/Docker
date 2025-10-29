FROM python:3.13.9-alpine3.21
MAINTAINER akshaybk85
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]



