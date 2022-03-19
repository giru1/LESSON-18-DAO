# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
