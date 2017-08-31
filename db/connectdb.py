# -*- coding: utf-8 -*-
import sqlite3

def create(dbname):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute('CREATE TABLE region (id INTEGER PRIMARY KEY, code_region INTEGER, name_region VARCHAR(30))')
    cur.execute('CREATE TABLE city (id INTEGER PRIMARY KEY, code_region INTEGER, code_city INTEGER, name_city VARCHAR(30))')
    cur.execute('CREATE TABLE coment (id INTEGER PRIMARY KEY, surname VARCHAR(50),'
                'firstName VARCHAR(50), patronymic VARCHAR(50), email VARCHAR(100), phone VARCHAR(14), code_city INTEGER,'
                'comment VARCHAR(500))')
    cur.execute('INSERT INTO region VALUES(NULL, "1", "Краснодарский край ")')
    cur.execute('INSERT INTO region VALUES(NULL, "2", "Ростовская область ")')
    cur.execute('INSERT INTO region VALUES(NULL, "3", "Ставропольский край")')
    cur.execute('INSERT INTO region VALUES(NULL, "4", "Не указан")')
    cur.execute('INSERT INTO city VALUES(NULL, "1",  "1", "Краснодар")')
    cur.execute('INSERT INTO city VALUES(NULL, "1",  "2", "Кропоткин")')
    cur.execute('INSERT INTO city VALUES(NULL, "1",  "3", "Славянск")')
    cur.execute('INSERT INTO city VALUES(NULL, "2",  "4", "Ростов")')
    cur.execute('INSERT INTO city VALUES(NULL, "2",  "5", "Шахты")')
    cur.execute('INSERT INTO city VALUES(NULL, "2",  "6", "Батайск")')
    cur.execute('INSERT INTO city VALUES(NULL, "3",  "7", "Ставрополь")')
    cur.execute('INSERT INTO city VALUES(NULL, "3",  "8", "Пятигорск")')
    cur.execute('INSERT INTO city VALUES(NULL, "3",  "9", "Кисловодск")')
    cur.execute('INSERT INTO city VALUES(NULL, "4",  "0", "Не указан")')
    con.commit()
    con.close()

