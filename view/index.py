# -*- coding: utf-8 -*-
from sysrender.render_html import *


def index(environ, start_response):
    """
    стартовая страница
    :param environ:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    kwards = {'title': 'Тестовая страница'}
    kwards['block_css'] = '<style>' + renderToStr('main.css', CSS_PATH) + '</style>'
    kwards['main_menu'] = renderToStr('main_menu.html', TEMPLATES_PATCH)
    kwards['block_js'] = '<script>' + renderToStr('main.js', JS_PATH) + '</script>'
    return [render_html('index.html', **kwards)]


def load_img(environ, start_response):
    start_response('200 OK', [('Content-Type', 'image/png')])
    return open(os.path.join(BASE_DIR, IMG_PATH, environ['myapp.url_args'][0]), "rb").read()
