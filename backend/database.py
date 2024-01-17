from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Item

class db:
    def __init__(self, db_url: str):
        self.offline = False
        try:
            self.engine = create_engine(db_url)
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = self.engine)
            Base.metadata.create_all(bind = self.engine)
        except:
            self.offline = True

    def connect(self):
        if self.offline:
            return None
        db = self.SessionLocal()
        try:
            return db
        finally:
            db.close()
