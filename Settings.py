# -*- coding: utf-8 -*-
import os

# стратовый путь для всех файлов
BASE_DIR = os.getcwd()

# папка с html шаблонами
TEMPLATES_PATCH = (
    'templates',
)

CSS_PATH = (
    'css',
)

JS_PATH = (
    'js',
)

IMG_PATH = 'images'

# паттерн используется для поисков тегов в тексте
PATTERN_TEMPLATE_TAG_RAW = "({{[_a-zA-Z 0-9]+}})"
PATTERN_TEMPLATE_TAG = "({{[ ]*&&[ ]*}})"
PATTERN_CLEAR_TAG = "(?:[ ]*)([_a-zA-Z 0-9]+)"