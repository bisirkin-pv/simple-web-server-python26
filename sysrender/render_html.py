# -*- coding: utf-8 -*-
import re
from Settings import *


def renderToStr(nameFile, SEARCH_PATCH):
    """
    Функция фозвращает строку html текста
    :param nameFile: имя html файла
    :param **kwargs: славарь для подстановки переменных
    :return: строковое представление шаблона
    """
    # ищем первый файл в папках шаблонов
    templatePatch = getTemplatePatch(SEARCH_PATCH, BASE_DIR, nameFile)
    if templatePatch == "":
        return ""
    template = open(os.path.join(templatePatch, nameFile), 'r').read()
    return template


def render_html(nameFile, **kwargs):
    """
    Функция фозвращает строку html текста
    :param nameFile: имя html файла
    :param **kwargs: славарь для подстановки переменных
    :return: строковое представление шаблона
    """
    # ищем первый файл в папках шаблонов
    templatePatch = getTemplatePatch(TEMPLATES_PATCH, BASE_DIR, nameFile)
    if templatePatch == "":
        return ""
    rawHtml = open(os.path.join(templatePatch, nameFile), 'r').read()
    replacedHtml = replaceInTemplate(rawHtml, PATTERN_TEMPLATE_TAG, kwargs)
    clearAndRplacedHtml = replaceInTemplate(replacedHtml, PATTERN_TEMPLATE_TAG_RAW, {})
    return clearAndRplacedHtml


def getTemplatePatch(tuplePatchTamplate, baseDir, findFile):
    """
    Возвращаем путь найденного файла
    :param tuplePatchTamplate: картеж папок с шаблонами
    :param baseDir: путь приложения
    :param findFile: файл для поиска
    :return:
    """
    templatePatch= ""
    if tuplePatchTamplate.__len__() > 0:
        for item in tuplePatchTamplate:
            pth = os.path.join(baseDir, item)
            if os.path.exists(os.path.join(baseDir, item)):
                if [item for item in os.listdir(pth) if item == findFile].__len__() > 0:
                    templatePatch = pth
                    break
    return templatePatch


def replaceInTemplate(template, pattern, dictForRaplace):
    """
    Функция производит подстановку простых переменных в html
    :param template: шаблон
    :param pattern: патерн для поиска (в нем && заменяется на ключ словаря)
    :param dictForRaplace: словарь для замены
    :return: строку с подставленными переменными
    """
    if dictForRaplace.__len__() > 0:
        for key, value in dictForRaplace.items():
            template = findAndReplace(pattern, template, key, value)
    else:
        template = findAndReplace(pattern, template)
    return template


def findAndReplace(pattern, template, key='', value=''):
    """
    Функция ищет и заменяет найденный текст в строке
    :param pattern: патерн для поиска (в нем && заменяется на ключ словаря)
    :param template: шаблон
    :param key: ключ для поиска
    :param value: значение для замены
    :return:
    """
    fndText = re.finditer(pattern.replace('&&', key), template)
    for item in fndText:
        for repl in item.groups():
            template = template.replace(repl, value)
    return template

