import json
# from demjson import decode
# import pandas as pd
import os
import csv
import requests
sitename1 = ''
inputconsole = ''
token = ''
cursorp = ''
counts = 0
cursortoken = ''
cursorloop = ''
indexCheck = False
if os.path.isfile("16INQXE5TJOIQFGZLDOVZGS5DZ.csv"):
    os.remove("16INQXE5TJOIQFGZLDOVZGS5DZ.csv")
if os.path.isfile("18JRGEYTCMJRCUKRKFIVJFEUSS.csv"):
    os.remove("18JRGEYTCMJRCUKRKFIVJFEUSS.csv")
with open('data') as f:
    for line in f:
        #print(line)



        cursorloop = {"cursor": cursortoken}
        myUrl2 = 'https://' + inputconsole + '.sentinelone.net/web/api/v2.0/application-inventory?siteIds='+ line +''

        head = {'Authorization': 'ApiToken {}'.format(token)}
        response = requests.get(myUrl2, headers=head)
        fjson = open('input_json.json', 'w')
        jsondata = response.json()
        fjson.write(json.dumps(jsondata))
        fjson.close()
        fjsonout = open ('input_json.json', 'r')
        for line2 in fjsonout:
            if 'Application' in line2:
                myUrl3 = 'https://'+inputconsole+'.sentinelone.net/web/api/v2.0/sites/'+line

                response2 = requests.get(myUrl3, headers=head)
                sitename1 = ''
                sitename = response2.json()['data']['name']
                if not  '_del_' in sitename:
                    sitename1 = sitename
                f3 = open ("Report.csv", 'a' , encoding='utf-8', newline='' )
                csvwriter = csv.writer(f3, delimiter=',')
                liste = {}
                if counts == 0:
                    header = 'Console', 'Site'
                liste['Console'] = inputconsole
                liste['Site'] = sitename

                csvwriter.writerow(liste.values())
                print (sitename1)

        fjsonout.close()
