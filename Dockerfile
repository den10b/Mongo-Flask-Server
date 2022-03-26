FROM python:3-onbuild

EXPOSE 5000

RUN pip install --upgrade pip

RUN flask db migrate -m "message table"

RUN flask db upgrade

CMD ["python", "./run.py"]

