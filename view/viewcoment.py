# -*- coding: utf-8 -*-
from urlparse import parse_qs
from sysrender.render_html import *
from Settings import CSS_PATH, JS_PATH
from db.workdb import Workdb
import json


def view(environ, start_response):
    """
    Страница отображения коментариев
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    kwards = {'title': 'Просмотр комментариев'}
    kwards['block_css'] = '<style>' + renderToStr('main.css', CSS_PATH) + '</style>'
    kwards['block_js'] = '<script>' + renderToStr('main.js', JS_PATH) + '</script>'
    kwards['main_menu'] = renderToStr('main_menu.html', TEMPLATES_PATCH)
    return [render_html('view.html', **kwards)]


def getviewcoment(environ, start_response):
    """
    Процедура получения комментариев
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/plan')])
    workDb = Workdb('test.db')
    comments = workDb.SelectComent()
    print(comments)
    tableRows = u'<table id="myTable" cellspacing="0">\
    <tr align="center">\
        <th>Фамилия</th>\
        <th>Имя</th>\
        <th>Отчество</th>\
        <th>Email</th>\
        <th>Телефон</th>\
        <th>Город</th>\
        <th>Коментарий</th>\
        <th>Действие</th>\
    </tr>'
    for line in comments:
        tableRows += u"<tr>"
        ind = -1
        for elem in line:
            if type(elem) != int:
                tableRows += u'<td>' + elem + u'</td>'
            else:
                ind = elem
        tableRows += u"<td><button id=" + unicode(str(ind), 'ascii') + u" onclick = deleteComment(this.id)>Удалить</button></td></tr>"
    tableRows += u'</table>'
    return json.JSONEncoder().encode({'name': tableRows})


def delcoment(environ, start_response):
    """
    Процедура удаления комментариев
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
    id = data['id']
    workDb = Workdb('test.db')
    workDb.DeleteComent(id)
    return ["Успешно"]