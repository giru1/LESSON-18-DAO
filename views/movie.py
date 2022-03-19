# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
