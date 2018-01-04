# coding:utf-8
import requests as rq
import json
import ast



# 引入 MySQLdb 模組，提供連接 MySQL 的功能
import pymysql as MySQLdb

# 連接 MySQL 資料庫
#db = MySQLdb.connect(host="xxx.xxxx.xxxx.xxxx",user="root", passwd="root_password", db="db_liat_name",charset='utf8')

def status():
    if db.open:
        print ('-- DB status: connection is open')
    else:
        print ('-- DB status: connection is closed')

def connectDB(Thost="localhost",Tuser="root", Tpasswd="root", Tdb="BSA",Tcharset='utf8'):
    print ("-- DB commend: connent to DB "+str(Thost))
    global db,cursor
    db = MySQLdb.connect(host=Thost,user=Tuser, passwd=Tpasswd, db=Tdb,charset=Tcharset)
    cursor = db.cursor()

def close():
    print("-- DB commend: close connection to DB")
    db.close()

def exeSQl(sql):
    print('-- SQL commend: '+str(sql))
    # 執行 MySQL 查詢指令
    cursor.execute(sql)
    db.commit()
    # 取回所有查詢結果
    results = cursor.fetchall()
    '''
    # 輸出結果
    for record in results:
        row = ""
        for col in record:
            row += str(col).replace("\n", "")
            row += ","        
        print row
    '''
    return results





connectDB("127.0.0.1","root","root","LoL",'utf8')

accountId = '151368953'

sql = 'SELECT DISTINCT `gameId` FROM `games` WHERE `accountId` = '+accountId
respond = exeSQl(sql)
    
close()

