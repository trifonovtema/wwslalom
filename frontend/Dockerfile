FROM python:3.11-bookworm

WORKDIR /code

COPY ./src /code/

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python3.11", "app.py"]