# -*- coding: utf-8 -*-
# __author__ = 'Бисиркин Павел'
from wsgiref.simple_server import make_server
import urls
import re
from db.connectdb import create
import os


def not_found(environ, start_response):
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Error 404. Запрашиваемая страница не найдена.']


# Начальные настройки базы
def create_base():
    create('test.db')


def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls.urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)

# Если базы данных нет, то создаем
if not os.path.exists(os.path.join(os.getcwd(), 'test.db')):
    create_base()
srv = make_server('localhost', 8080, application)
srv.serve_forever()
