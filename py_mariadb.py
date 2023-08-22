#!/usr/bin/python3
#-*-coding:utf-8-*-

import os,sys
import pymysql
import mariadb
from threading import Timer
import time
import datetime
import schedule

mysql_host = os.environ.get("MARIADB_HOST")
mysql_post = int(os.environ.get("MARIADB_PORT"))
mysql_user = os.environ.get("MARIADB_USER")
mysql_pwd = os.environ.get("MARIADB_PASSWORD")
mysql_database = os.environ.get("MARIADB_DATABASE")

def prtime():
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
prtime()
 
#db = mariadb.connect(host="10.80.28.13",port=3307,user="root",passwd="123456",database="testdb")
def connect():
    print("in connect")
    #db = mariadb.connect(host="10.80.28.13",port=3307,user="root",passwd="123456",database="testdb")

    db = mariadb.connect(host=mysql_host,port=mysql_post,user=mysql_user,passwd=mysql_pwd,database=mysql_database)
    #使用 cursor() 方法创建一个游标对象
    cursor = db.cursor()
    #使用 execute() 方法执行 SQL 查询
    cursor.execute("SELECT * FROM info")
    #使用 fetchone() 方法获取单条数据
    data = cursor.fetchall()
    def Mon():
        for one in data:
            print(one)
        prtime()
    Timer(3,Mon).start()
    prtime()
    #Timer(120,prtime).start()
        #time.sleep(120)
    #关闭数据库连接
    cursor.close()
    db.close()

connect()
#Timer(120,prtime).start();
#time.sleep(120)
