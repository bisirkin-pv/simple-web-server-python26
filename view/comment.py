# -*- coding: utf-8 -*-
from urlparse import parse_qs
from sysrender.render_html import *
from Settings import CSS_PATH, JS_PATH
from db.workdb import Workdb
import json


def comment(environ, start_response):
    """
    Страница отображения комментариев
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    kwards = {'title': 'Тестовая страница'}
    kwards['block_css'] = '<style>' + renderToStr('main.css', CSS_PATH) + '</style>'
    kwards['block_js'] = '<script>' + renderToStr('main.js', JS_PATH) + '</script>'
    kwards['main_menu'] = renderToStr('main_menu.html', TEMPLATES_PATCH)
    return [render_html('comment.html', **kwards)]


def save(environ, start_response):
    """
    Процедура сохранения комментариев в базу
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/plan')])
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)
    data = parse_qs(request_body)
    try:
        surname = data['surname'][0].decode('utf8')
    except:
        surname = 'not'
    try:
        firstName = data['firstName'][0].decode('utf8')
    except:
        firstName = 'not'
    try:
        patronymic = data['patronymic'][0].decode('utf8')
    except:
        patronymic = 'не указано'.decode('utf8')
    try:
        email = data['email'][0].decode('utf8')
    except:
        email = 'не указано'.decode('utf8')
    try:
        phone = data['phone'][0].decode('utf8')
    except:
        phone = 'не указано'.decode('utf8')
    if (data['code_city'][0] == 'not'):
        code_city = 0
    else:
        code_city = data['code_city'][0]
    try:
        comment = data['comment'][0].decode('utf8')
    except:
        comment = 'not'
    if (surname == "not") or (firstName == "not") or (comment == "not"):
        return ["Не заполнены поля"]
    workDb = Workdb('test.db')
    workDb.InsertComent(surname, firstName, patronymic, email, phone, code_city, comment)
    return ["Успешно"]


def getregion(environ, start_response):
    """
    Процедура получения списка регионов
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/plan')])
    workDb = Workdb('test.db')
    name = workDb.SelectRegion()
    return json.JSONEncoder().encode({'name': name})


def getcity(environ, start_response):
    """
    Процедура получения списка городов по выбранному региону
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/plan')])
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)
    data = parse_qs(request_body)
    workDb = Workdb('test.db')
    codeRegion = data['city'][0]
    name = workDb.SelectCity(str(codeRegion))
    return json.JSONEncoder().encode({'name': name})

