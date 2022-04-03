from typing import Dict, Any

from marshmallow import Schema

from lib.dao import BaseDAO



class BaseService:

    def __init__(self, dao: BaseDAO, schema: Schema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, id: int):
        return self.schema.dump(self.dao.get_one(id))

    def create(self, data: Dict[str, Any]):
        return self.dao.create(data=self.schema.load(data))

    def update(self, id: int, data: Dict[str, Any]):
        self.dao.update(id, self.schema.load(data))

    def delete(self, id: int):
        self.dao.delete(id)
