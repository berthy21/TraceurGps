FROM python:2.7-slim

WORKDIR /Bureau/TraceurGps

EXPOSE  80

CMD ["python","manage.py"]