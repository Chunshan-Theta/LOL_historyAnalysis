# coding:utf-8
import requests as rq
import json
import ast

data = json.loads((rq.get("https://www.masterypoints.com/api/v1.1/static/champions").content).decode('utf-8'))
#print(data)
ind = 1
for i in data.keys():
    print(ind,i)
    ind+=1









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
#print(exeSQl("INSERT INTO `champion` (`id`, `name`, `title`, `chinese_name`) VALUES ('1', '1', '1', '1');"))

for i in data.values():
    cid = str(i["id"])
    cname = str(i["name"])
    ctitle = str(i["title"])
    try:
        sql = 'INSERT INTO `champion` (`id`, `name`, `title`, `chinese_name`) VALUES ("'+cid+'", "'+cname+'", "'+ctitle+'", "init");'
        print(exeSQl(sql))
    except Exception as e:
        print(e)
    
close()

