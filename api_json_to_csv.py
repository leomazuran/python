import requests
import json
import csv
import os
inputconsole = 'INPUT CONSOLE SUBDOMAIN '
token = 'API TOKEN'
cursorp = ''
counts = 0
cursortoken = ''
cursorloop = ''
indexCheck = False
if os.path.isfile("16INQXE5TJOIQFGZLDOVZGS5DZ02.csv"):
        os.remove("16INQXE5TJOIQFGZLDOVZGS5DZ02.csv")
if os.path.isfile("18JRGEYTCMJRCUKRKFIVJFEUSS02.csv"):
        os.remove("18JRGEYTCMJRCUKRKFIVJFEUSS02.csv")
with open('idlist2.txt') as f:
    for line in f:
        print (line)
        
        while True:
               
                cursorloop = {"cursor":cursortoken}
                myUrl2 = 'https://'+inputconsole+'.myurl.net/web/api/v2.0/exclusions?skipCount=false&countOnly=false&limit=100&siteIds='+line+'&type=path'
                head = {'Authorization': 'ApiToken {}'.format(token)}
               # print (myUrl2)
                

                response2 = requests.get(myUrl2, headers=head, params=cursorloop)
                #cursortoken = str(response2.json()['pagination']['nextCursor'])
                #print (cursortoken)
                #print (str(response.json()))
                try:
                    if not str(response2.json()['pagination']['nextCursor']) == None or "None":
                        print ("next")
                        print (str(response2.json()['pagination']['nextCursor']))
                        cursortoken = str(response2.json()['pagination']['nextCursor'])
                        cursorloop = {'cursor':cursortoken}


                    else: 
                        print ("No more next")
                        cursortoken = ''
                        break
                except:
                    print ('pagination null')
                    cursortoken = ''
                    break
                      ##TODO Fix this.
                
                        #print (cursorloop)
               
               
                        

                
               
                fh = open('17ONVWU3DENRZHK2TENNSGW4TL02.json', 'w')
                fhdata = response2.json()

                fh.write(json.dumps(fhdata))

                fh.close()


                f2 = open ('17ONVWU3DENRZHK2TENNSGW4TL02.json')
                data2 = json.load(f2)
                f2.close()
                datawrite = data2['data']

                f3 = open('16INQXE5TJOIQFGZLDOVZGS5DZ02.csv', 'a', encoding='utf-8')
                csvwriter = csv.writer(f3, delimiter =',')
                liste={}
                t = str('file')
                f = str('FALSE')
                end = ''
                for item in datawrite:
                        if counts == 0:
                                header = 'scope','group','value'
                                csvwriter.writerow(header)
                                counts += 1
                        
                     
                        liste['scope'] = item['scopeName']
                        site = item['scopeName']
                        #print ("Getting exclusion for "+site+".")
                        liste['group'] = ''
                        liste['value'] = item['value']
                     
                        csvwriter.writerow(liste.values())
                f3.close()
                
                group_parout = {'siteIds': line}
                so = requests.get('https://'+inputconsole+'.myurl.net/web/api/v2.0/groups?skipCount=false&countOnly=false&limit=200', headers=head, params=group_parout)


                #print (so.json())
                if not so.json()['pagination']['totalItems'] == '0':
                    
                        print ('\n There are currently '+str(so.json()['pagination']['totalItems'])+' groups in your site. \n')
                        frgroup= open('13K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json', 'w')
                        datagroup = so.json()
                        frgroup.write(json.dumps(datagroup))
                        #print (json.dumps(datagroup))
                        print ("\n\nGetting Group exclusion.....\n\n")
                        frgroup.close()
                        f3 = open ('13K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json')
                        data3 = json.load(f3)
                        f3.close()
                        groupwrite = data3['data']
                        for item2 in groupwrite:

                            #fgroup = open ('grouplistdprok3409idkf3.csv', 'w')
                            #csvwriter = csv.writer(fgroup, delimiter =',')
                            groupliste5 = {}
                            groupliste5['id']= item2['id']
                            #print (groupliste5.values())
                            policy_parout = { 'groupIds': groupliste5.values()}

                            myUrl= 'https://'+inputconsole+'.myurl.net/web/api/v2.0/exclusions?skipCount=false&countOnly=false&limit=100&type=path'
                            

                            response = requests.get(myUrl, headers=head, params=policy_parout)
                          
                            
                           
                           
                           
                                    

                            f= open('16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF02.json', 'w')
                            data = str(response.json())
                            data1 = response.json()
                            f.write(json.dumps(data1))
                            f.close()
                            
                            f2 = open ('16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF02.json')
                            data2 = json.load(f2)
                            f2.close()
                            datawrite1 = data2['data']

                            f3 = open('16INQXE5TJOIQFGZLDOVZGS5DZ02.csv', 'a', encoding='utf-8')
                            csvwriter = csv.writer(f3, delimiter =',')
                            liste1={}
                           
                            end = ''
                            for item3 in datawrite1:
                                    
                                    
                                    liste1['scope'] = site
                                    liste1['scopeName'] = item3['scopeName']
                                    
                                    liste1['value'] = item3['value']
                                    
                                    
                                    csvwriter.writerow(liste1.values())
                        f3.close()
                

f.close()
#Developer: Leonardo Mazuran
