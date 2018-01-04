# coding:utf-8
import requests as rq
import json





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
    #print('-- SQL commend: '+str(sql))
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
import sys
print(sys.argv[1])
name = sys.argv[1]
data = json.loads((rq.get("https://acs-garena.leagueoflegends.com/v1/players?name="+name+"&region=TW").content).decode("utf-8"))


accountId = str(data['accountId'])
begIndex =1
patch = 20
gameCount = 30
while(int(gameCount) > int(begIndex)):
    
    connectDB("127.0.0.1","root","root","LoL",'utf8')
    #print(exeSQl("INSERT INTO `champion` (`id`, `name`, `title`, `chinese_name`) VALUES ('1', '1', '1', '1');"))
    print(accountId,":",begIndex,'~',begIndex+patch,'/',gameCount)
    data = (rq.get("https://acs-garena.leagueoflegends.com/v1/stats/player_history/TW/"+accountId+"?begIndex="+str(begIndex)+"&endIndex="+str(begIndex+patch)).content).decode("utf-8") 
    #print(data.content)
    
     

    data_json = json.loads(data)
    games = data_json['games']
    game= games['games']

    '''
    for key in data_json.keys():
        print(key)

    print('+'*20)

    
    for key in games:
        print(key)
    print('+'*20)
    '''



    try:
        accountId = str(data_json['accountId'])#player-1
        platformId = str(data_json['platformId'])#player-2
        summonerName = str(games['games'][0]['participantIdentities'][0]['player']['summonerName'])#player-3
        gameCount = str(games['gameCount'])#player-4

        accountId = str(data_json['accountId'])#player-1
        sql = 'INSERT INTO `player` (`accountId`, `platformId`, `summonerName`, `gameCount`) VALUES ("'+accountId+'", "'+platformId+'", "'+summonerName+'", "'+gameCount+'");'
        print(exeSQl(sql))
    except Exception as e:
        print(e)
        try:
            print('try to update')
            sql = 'UPDATE `player` SET `gameCount` = "'+gameCount+'" WHERE `player`.`accountId` = "'+accountId+'";'
            exeSQl(sql)
        except Exception as e:
            print(e)
    try:
        for key_1 in game:
            #print(key_1)
            #print('+'*20)
            gameId = str(key_1['gameId'])#game-1
            gameCreation = str(key_1['gameCreation'])#game-2
            gameMode = str(key_1['gameMode'])#game-3
            championId = str(key_1['participants'][0]['championId'])#game-4
            Detail = str(key_1)#game-5
            win =str(key_1['participants'][0]['stats']['win'])

            sql = 'INSERT INTO `games` (`id`,`gameId`,`accountId`, `gameCreation`, `gameMode`, `championId`,`win`, `Detail`) VALUES (NULL,"'+gameId+'","'+accountId+'","'+gameCreation+'", "'+gameMode+'", "'+championId+'","'+win+'","'+Detail+'");'
            exeSQl(sql)
    except Exception as e:
        print(e)
    close()
    begIndex+=patch
    























