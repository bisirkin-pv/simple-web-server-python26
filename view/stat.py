# -*- coding: utf-8 -*-
from urlparse import parse_qs
from sysrender.render_html import *
from Settings import CSS_PATH, JS_PATH
from db.workdb import Workdb
import json


def stat(environ, start_response):
    """
    Страница отображения коментариев
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    kwards = {'title': 'Просмотр статистики'}
    kwards['block_css'] = '<style>' + renderToStr('main.css', CSS_PATH) + '</style>'
    kwards['block_js'] = '<script>' + renderToStr('main.js', JS_PATH) + '</script>'
    kwards['main_menu'] = renderToStr('main_menu.html', TEMPLATES_PATCH)
    return [render_html('stat.html', **kwards)]


def statcomentfive(environ, start_response):
    """
    Процедура вывода регионов содержащих более 5 комментариев
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/plan')])
    workDb = Workdb('test.db')
    name = workDb.StatRegionCountFive()
    return json.JSONEncoder().encode({'name': name})


def statcomentall(environ, start_response):
    """
    Процедура вывода всех регионов с комментриями
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/plan')])
    workDb = Workdb('test.db')
    name = workDb.StatRegionAll()
    return json.JSONEncoder().encode({'name': name})


def getstatcomentcity(environ, start_response):
    """
    Процедура вывода городов региона с комментриями
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
    region_id = data['region_id'][0].decode('utf8')
    workDb = Workdb('test.db')
    name = workDb.StatCityRegion(region_id)
    return json.JSONEncoder().encode({'name': name})
