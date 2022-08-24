from ast import Delete

from sqlalchemy.orm import Session

class ReposityProduct():
    def __init__(self, db: Session):
        self.db = db
    def create(self):
        pass
    def list(self):
        pass
    def remove(self):
        pass
