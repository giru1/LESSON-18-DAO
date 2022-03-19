# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
