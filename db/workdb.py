# -*- coding: utf-8 -*-
import sqlite3


class Workdb:
    def __init__(self, dbName):
        self.dbName = dbName
        self.con = sqlite3.connect(self.dbName)
        self.cur = self.con.cursor()

    def InsertComent(self, Surname, firstName, patronymic, email, phone, code_city, comment):
        self.cur.execute('INSERT INTO coment VALUES(NULL, ?,?,?,?,?,?,?)',
                         (Surname, firstName, patronymic, email, phone, code_city, comment))
        self.con.commit()
        self.con.close()

    def DeleteComent(self, id):
        self.cur.execute('DELETE FROM coment WHERE id = ?', id)
        self.con.commit()
        self.con.close()

    def SelectRegion(self):
        self.cur.execute('SELECT code_region, name_region FROM region WHERE code_region != 4')
        return self.cur.fetchall()

    def SelectCity(self, code_region):
        self.cur.execute('SELECT code_city, name_city FROM city WHERE code_region = ?', code_region)
        return self.cur.fetchall()

    def SelectComent(self):
        self.cur.execute('SELECT coment.id, surname, firstName, patronymic, email, phone, city.name_city ,comment '
                         'FROM coment INNER JOIN city ON city.code_city = coment.code_city ORDER BY coment.id DESC ')
        return self.cur.fetchall()

    def StatRegionCountFive(self):
        self.cur.execute('SELECT region.name_region, count(region.name_region) FROM coment '
                         'INNER JOIN city ON city.code_city = coment.code_city '
                         'INNER JOIN region ON region.code_region = city.code_region '
                         'GROUP BY region.name_region HAVING count(region.name_region) >= 5 ')
        return self.cur.fetchall()

    def StatRegionAll(self):
        self.cur.execute('SELECT region.id, region.name_region, count(region.name_region) FROM coment '
                         'INNER JOIN city ON city.code_city = coment.code_city '
                         'INNER JOIN region ON region.code_region = city.code_region '
                         'GROUP BY region.name_region ')
        return self.cur.fetchall()

    def StatCityRegion(self, region_id):
        self.cur.execute('SELECT name_city, count(comment) FROM coment '
                         'INNER JOIN city ON city.code_city = coment.code_city '
                         'INNER JOIN region ON region.code_region = city.code_region '
                         'GROUP BY city.name_city '
                         'HAVING region.code_region == ?', region_id)
        return self.cur.fetchall()
