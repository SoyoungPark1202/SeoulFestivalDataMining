#-*- coding:utf-8 -*-
import cx_Oracle
import os

os.environ["NLS_LANG"] = ".AL32UTF8"

START_VALUE = u"Unicode \u3042 3".encode('utf-8')
END_VALUE = u"Unicode \u3042 6".encode('utf-8')

con = cx_Oracle.connect('java08/java08@192.168.137.201:1521/orcl')
cur = con.cursor()
cur.execute('select * from food1 order by num desc')

row = cur.fetchone()

if row:
    while row:
        print(row)
        row = cur.fetchone()

cur.close()
con.close()

# #-*- coding:utf-8 -*-
# import cx_Oracle
# import os
#
#
# os.environ["NLS_LANG"] = ".AL32UTF8"
#
# START_VALUE = u"Unicode \u3042 3".encode('utf-8')
# END_VALUE =  u"Unicode \u3042 6".encode('utf-8')
#
# def ConDB():
#   db = cx_Oracle.connect('java08/java08@192.168.137.201:1521/orcl')
#   cur = db.cursor()
#   cur.execute("select * from food1 order by num desc")
#   for result in cur:
#       print(result,'euc-kr')
#
# if __name__=="__main__":
#     ConDB()