# -*- coding: utf-8 -*-
from view.index import index, load_img
from view.comment import comment, save, getregion, getcity
from view.viewcoment import view, getviewcoment, delcoment
from view.stat import stat, statcomentfive, statcomentall, getstatcomentcity

urls = [
    (r'^$', index),
    (r'stat/$', stat),
    (r'stat/statcomentfive/(.*)$', statcomentfive),
    (r'stat/statcomentall/(.*)$', statcomentall),
    (r'stat/statcomentcity/(.*)$', getstatcomentcity),
    (r'view/$', view),
    (r'view/getviewcoment/(.*)$', getviewcoment),
    (r'view/delcoment/(.*)$', delcoment),
    (r'comment/$', comment),
    (r'comment/getregion/(.*)$', getregion),
    (r'comment/getcity/(.*)$', getcity),
    (r'comment/save/(.*)$', save),
    (r'images/(.*)$', load_img)

]