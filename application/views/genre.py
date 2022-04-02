# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace
from application.setup_db import db
from application.dao.model import genre
genres_ns = Namespace('genre')


@genres_ns.route('/')
class GenreView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
