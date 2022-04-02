from typing import Dict, Any

from lib.dao import BaseDAO
from application.dao.model.genre import Genre


class GenresDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()