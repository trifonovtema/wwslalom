Local development:
```shell
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
```

How to run in container:
```shell
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
docker compose --env-file ./.env up -d
alembic upgrade head
```

Work with containers
```shell
docker compose --env-file ./.env up -d
docker compose down
docker compose build  
```

Work with Alembic
```shell
alembic init alembic
alembic upgrade head
alembic revision -m "your migration description" --autogenerate --head head
alembic downgrade base

```

Work woth FastAPI
```shell
uvicorn --app-dir=./backend/src/ main:app --reload
ps aux | grep uvicorn
kill -9
```


Work with flet
```shell
flet ./app.py
flet -w ./app.py  
python ./app.py
```
