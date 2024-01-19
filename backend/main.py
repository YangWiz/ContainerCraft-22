from fastapi import FastAPI, Depends
from schemas import Item, UpdateItem
from sqlalchemy.orm import Session
from database import db
from models import Base
import logging
import models
import os

logging.basicConfig(filename="todolist.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
# get root logger
logger = logging.getLogger(__name__)

ENV_VAR_DB_HOST = "DB_HOST"
ENV_VAR_DB_PORT = "DB_PORT"
ENV_VAR_DB_NAME = "POSTGRES_DB"
ENV_VAR_DB_USERNAME = "POSTGRES_USER"
ENV_VAR_DB_PASSWORD = "POSTGRES_PASSWORD"

db_host = os.getenv(ENV_VAR_DB_HOST, "localhost")
db_port = os.getenv(ENV_VAR_DB_PORT, "5432")
db_name = os.getenv(ENV_VAR_DB_NAME, "postgres")
db_username = os.getenv(ENV_VAR_DB_USERNAME, "postgres")
db_password = os.getenv(ENV_VAR_DB_PASSWORD, "test")

db_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

logger.info(f"got url from envs: {db_url}")
psql = db(db_url)
app = FastAPI()

@app.get("/list")
def read_list(db: Session = Depends(psql.connect)):
    return db.query(models.Item).all()

@app.post("/list")
def add_item(item: Item, db: Session = Depends(psql.connect)):
    new_item = models.Item(name = item.name, description = item.description, complete = False)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/list/{item_id}")
def read_item(item_id: int, db: Session = Depends(psql.connect)):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

@app.delete("/list/{item_id}")
def delete_item(item_id: int, db: Session = Depends(psql.connect)):
    curr_item = db.query(models.Item).filter(models.Item.id == item_id).one_or_none()
    if curr_item is None:
        return None
    db.delete(curr_item)
    db.commit()
    return curr_item

@app.put("/list")
def update_item(item: UpdateItem, db: Session = Depends(psql.connect)):
    curr_item = db.query(models.Item).filter(models.Item.id == item.id).one_or_none()
    if curr_item is None:
        return None

    for var, value in vars(item).items():
        setattr(curr_item, var, value) if value is not None else None

    db.add(curr_item)
    db.commit()
    db.refresh(curr_item)
    return curr_item

@app.put("/list/incomplete/{item_id}")
def mark_task_imcomplete(item_id: int, db: Session = Depends(psql.connect)):
    curr_item = db.query(models.Item).filter(models.Item.id == item_id).one_or_none()
    if curr_item is None:
        return None

    setattr(curr_item, "compelete", False)

    db.add(curr_item)
    db.commit()
    db.refresh(curr_item)
    return curr_item

@app.put("/list/complete/{item_id}")
def mark_task_complete(item_id: int, db: Session = Depends(psql.connect)):
    curr_item = db.query(models.Item).filter(models.Item.id == item_id).one_or_none()
    if curr_item is None:
        return None

    setattr(curr_item, "compelete", True)

    db.add(curr_item)
    db.commit()
    db.refresh(curr_item)
    return curr_item
