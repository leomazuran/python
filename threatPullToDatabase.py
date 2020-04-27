import datetime
import re
import json
import urllib
import sys
import pymysql
import requests
from pytz import timezone
import time
import os
import arrow
token=""

def mysql ():
    print ("mysql")
def api_check ():
    time.sleep(15)
    api()
def api_loop ():
    time.sleep(2)
    api()

def api ():
    while True:
        current_time = datetime.datetime.utcnow().isoformat()+"Z"
        print (current_time)

        if os.path.isfile("time_left.msp02"):
            get_time = open ("time_left.msp02", "r")
            saved_time = get_time.readline()
        else:
            saved_time = "2019-12-25T00:00:00.000000Z"


        MSP02 = "https://carvir-msp02.sentinelone.net/web/api/v2.0/threats?skipCount=false&limit=100&countOnly=false&createdAt__gt="+saved_time+"&sortBy=createdAt"
        MSP = ""
        while True:
            head = {'Authorization': 'ApiToken {}'.format(token)}
            responseBB=requests.get(MSP02, headers=head)
            if responseBB.status_code !=200:
                print(("Error: %s") % responseBB.json())
                print ("error getting report!")
                time.sleep(10)
            elif responseBB.json()['pagination']['totalItems'] ==0:
                print ("Nothing yet!")
                time.sleep(10)
                
            else:
                break
                
            
        if responseBB.status_code == 200:
            total_count = responseBB.json()['pagination']['totalItems']
            print (total_count)
            if total_count != 0:
                print ("test")
                print(responseBB.json()['pagination']['totalItems'])
                if total_count >= 100:
                    total_count = 100
                    print (total_count)
                for row in range(total_count):

                    z_time =responseBB.json()['data'][row]['createdAt']
                    e_time = arrow.get(z_time).to("America/New_York").format('YYYY-MM-DD HH:mm:ss.SSSSSS')

                    ip_str =  responseBB.json()['data'][row]['agentIp']
                    ip_str_save = str(responseBB.json()['data'][row]['agentIp'])
                    ip_str = ip_str.replace(" ", "")
                    print (ip_str)
                    [a, b, c, d] = ip_str.split('.')
                    a = int(a)
                    b = int(b)
                    c = int(c)
                    d = int(d)
                    # check if IP Address is valid
                    assert 0 <= a <= 255
                    assert 0 <= b <= 255
                    assert 0 <= c <= 255
                    assert 0 <= d <= 255
                    ip_number = 16777216 * a + 65536 * b + 256 * c + d
                    print(ip_number)

                    mydb = pymysql.connect(
                        host="",
                        port=3306,
                        user="",
                        password="",
                        database="s1",
                        use_unicode=True
                    )
                    
                    print(str(responseBB.json()['data'][row]['fileDisplayName']),)
                    print (e_time)
                    
                        
                        
                    add_threat=("INSERT INTO threat (ComputerName, agentOSType, version, IPAddr, classification, fileDisplayName, filePath, SiteName, Console, DateTime, S_ID)"
                                            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    data_threat = (str(responseBB.json()['data'][row]['agentComputerName']),str(responseBB.json()['data'][row]['agentOsType']), str(responseBB.json()['data'][row]['agentVersion']),responseBB.json()['data'][row]['agentIp'],
                                                str(responseBB.json()['data'][row]['classification']), str(responseBB.json()['data'][row]['fileDisplayName']), str(responseBB.json()['data'][row]['filePath']), str(responseBB.json()['data'][row]['siteName']), 'MSP02', e_time, "https://carvir-msp02.sentinelone.net/analyze/threats/"+str(responseBB.json()['data'][row]['id']+"/overview"))
                    print (add_threat)
                    print (data_threat)
                    mydb.cursor().execute(add_threat, data_threat)
                    mydb.commit()
                 
                    cursorObject = mydb.cursor()
                    get_location_cache = ("Select lat, lon FROM ip_list WHERE IPCode = %s")
                    get_location_cache_input = (ip_number)
                    cursorObject.execute(get_location_cache, get_location_cache_input)
                    cache_row = cursorObject.fetchone()
                    print(cache_row)

                    if cache_row == None:
                        get_location = (
                            "Select latitude, longitude FROM ipmap.ip2location_db5_Disk WHERE ip_to >= %s and ip_from <= %s")
                        get_location_input = (ip_number, ip_number)
                        cursorObject.execute(get_location, get_location_input)
                        row = cursorObject.fetchone()
                        get_lat = (row[0])
                        get_lon = (row[1])
                        print (get_lat,get_lon)
                        set_location = ("Insert INTO ip_list (IPCode,IPAddr,Lat,Lon) VALUES (%s,%s,%s, %s)")
                        set_location_input = (ip_number,ip_str,get_lat, get_lon)
                        mydb.cursor().execute(set_location,set_location_input)
                        mydb.commit()
                        
                    else:
                        print("Already saved")

                last_time = responseBB.json()['data'][total_count-1]['createdAt']
                save_time = open ("time_left.msp02", "w")
                save_time.write(last_time)
                save_time.close()
                mydb.close()


           


api()



