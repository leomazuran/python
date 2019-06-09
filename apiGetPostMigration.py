#Author: Leonardo Mazuran (leonardo.mazuran@gmail.com)
import requests
import json
import csv
import time
#from demjson import decode
import pandas as pd
import re
import os
import base64
console1 = 'console1'
console2 ='console2'
console3 ='console3'
console4 = 'console4'
console5 = 'console5'
inputconsole = ''
inputchoice = ''
inputkey = ''
inputsite = ''
site_id = ''
gln = ''
input_token = ''
print('Beta Test 0.1.06\n')
print ('Developer: Leonardo Mazuran\n')
print('Please input source site token \n\n')

##
valid_character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789='



##

while True:
        try:
                inputchoice = ''
                inputchoice = input("Site Token: ")
                if all (char in valid_character for char in inputchoice):
                        input_token = inputchoice
                        pick = str(base64.b64decode(inputchoice))
                        #print (pick)
                        if "\"https://console1.myurl.net\"" in pick:
                                
                                inputconsole = console1
                                
                                break
                        elif "\"https://console2.myurl.net\"" in pick:
                                inputconsole = console2
                                
                                break
                        elif "\"https://console3.myurl.net\"" in pick:
                                inputconsole = console3
                                
                                break
                        elif "\"https://console4.myurl.net\"" in pick:
                                inputconsole = console4
                                
                                break
                        elif "\"https://console5.myurl.net\"" in pick:
                                inputconsole = console5
                                
                                break
                        else:
                                print ('\n Incorrect Site Token, Please try again!\n')
        except:
                print("Input error! Missing equal sign? Base 64 only, Thanks!")
#print (inputconsole)
            
##Authenticate

while True:
        
        print ('Please input API Key for '+inputconsole+'.')
        inputkey = input('Key: ')
        
        if all (char in valid_character for char in inputkey):
                AUTHURL = 'https://'+inputconsole+'.myurl.net/web/api/v2.0/private/user-info'
                headAUTH = {'Authorization': 'ApiToken {}'.format(inputkey)}
                authcheck = requests.get(AUTHURL, headers=headAUTH)
                print ('Checking key')
                if str(authcheck) == "<Response [401]>":
                        print ('Key is not valid for '+inputconsole+'.')
                elif str(authcheck) == "<Response [200]>":
                        print ("\n\nKey is valid. \n\n\n")
                        if not authcheck.json()['data']['role'] == 'admin':
                                print("However, you are not a Global Administrator.\n\n\n\n")
                                time.sleep(3)
                                print ("GoodBye!!!!")
                                time.sleep(2)
                                exit(1)
                        elif authcheck.json()['data']['role'] == 'admin':
                                break
               
                else:
                        print ("Please Try Again.")
                                                        
## Get Site	

try:
        


        params = {"registrationToken": input_token}  
        r = requests.get('https://'+inputconsole+'.myurl.net/web/api/v2.0/sites?limit=100', headers=headAUTH, params=params)
       
        if r.status_code != 200:
                print (("Error: %s") % r.json())
        
        if not r.json()['data']:
                print("No site found!")
                time.sleep(3)
                print ("GoodBye!")
                time.sleep(2)
                exit(1)
        if r.status_code == 200:
                site_id = r.json()['data']['sites'][0]['id']
                if r.json()['data']['sites'] [0] ['name']:
                        print("Site Found")
                        if r.json()['data']['sites'][0]['state'] == 'active':
                                print ("\n\n\n")

                                print ("Site Info that has been selected:\n")
                                print ("Site Name: "+r.json()['data']['sites'][0]['name']+'\n')
                                try:
                                        print ("Site Creator: "+r.json()['data']['sites'][0]['creator']+'\n')
                                except:
                                        print ("Not able to get Creator's Name. Love Dan!\n")
                                print ("Site ID: "+site_id+"\n")
                                
                                
                                
                        
## TODO While loop on the hole process.  (Console, Auth, Site)                                      
                        
except IndexError as indexerr:
        print ("No Site Found.")
try:
        group_par = {'siteIds': site_id}
        s = requests.get('https://'+inputconsole+'.myurl.net/web/api/v2.0/groups?skipCount=false&countOnly=true&limit=200', headers=headAUTH, params=group_par)
#print (group_par)
#print (s.json())

        if not s.json()['pagination']['totalItems'] == '0':
                print ('\n There are currently '+str(s.json()['pagination']['totalItems'])+' groups in your site. \n')
                
                        
                        
        
except:
        print ("Error, Failed to get Group Count")
        exit(1)


##TODO Check valid site check groups for adding
##TODO. Ask for Group
##TODO. Get a lit of groups for site.
outputconsole = ''
outputchoice = ''
outputkey = ''
outputsite = ''
outsite_id = ''
#print (input_token)
while True:
        try:
                print ("Please input destination site token.\n\n")
                outputchoice = ''
                outputchoice = input("Site Token: ")
                if all (char in valid_character for char in outputchoice):
                        output_token = outputchoice
                        pick1 = str(base64.b64decode(outputchoice))
                        #print (output_token)
                        if input_token in output_token:
                                print ("Source and Destination tokens are the same")
                        elif "\"https://console1.myurl.net\"" in pick1:
                                
                                outputconsole = console1
                                
                                break
                        elif "\"https://console2.myurl.net\"" in pick1:
                                outputconsole = console2
                                
                                break
                        elif "\"https://console3.myurl.net\"" in pick1:
                                outputconsole = console3
                                
                                break
                        elif "\"https://console4.myurl.net\"" in pick1:
                                outputconsole = console4
                                
                                break
                        elif "\"https://console5.myurl.net\"" in pick1:
                                outputconsole = console5
                                
                                break
                        
                        else:
                                print ('\n Incorrect Site Token, Please try again!\n')
        except:
                print("Input error! Missing equal sign? Base 64 only, Thanks!")


while True:
	
	print ('Please input API Key for '+outputconsole+'.')
	outputkey = input('Key: ')
	
	if all (char in valid_character for char in outputkey):
		AUTHURLOUT = 'https://'+outputconsole+'.myurl.net/web/api/v2.0/private/user-info'
		headAUTHOUT = {"Content-type": "application/json",'Authorization': 'ApiToken {}'.format(outputkey)}
		authcheckout = requests.get(AUTHURLOUT, headers=headAUTHOUT)
		print ('Checking key')
		if str(authcheckout) == "<Response [401]>":
			print ('Key is not valid for '+outputconsole+'.')
		elif str(authcheckout) == "<Response [200]>":
			print ("Key is valid.")
			break
		else:
			print ("Please Try Again.")
## Get Site	
while True:
        try:
               
                
                paramsout = {"registrationToken": output_token}  
                ro = requests.get('https://'+outputconsole+'.myurl.net/web/api/v2.0/sites?limit=100', headers=headAUTHOUT, params=paramsout)
               
                if ro.status_code != 200:
                        print (("Error: %s") % ro.json())
                
                if not ro.json()['data']:
                        print("No site found!")
                if ro.status_code == 200:
                        outsite_id = ro.json()['data']['sites'][0]['id']
                        if ro.json()['data']['sites'] [0] ['name']:
                                print("Site Found")
                                if ro.json()['data']['sites'][0]['state'] == 'active':
                                        print ("\n\n\n")

                                        print ("Site Info that has been selected:\n")
                                        print ("Site Name: "+ro.json()['data']['sites'][0]['name']+'\n')
                                        try:
                                                print ("Site Creator: "+ro.json()['data']['sites'][0]['creator']+'\n')
                                        except:
                                                print ("Not able to get Creator's Name. Love Dan!\n")
                                        print ("Site ID: "+outsite_id+"\n")
                                        print ('\n\n')
                                        break
                                        
                                elif not ro.json()['data']['sites'][0]['state'] == 'active':
                                        print ("Cant proceed, This site is "+ro.json()['data']['sites'][0]['state']+". Try a different site")
                                                
                                
        except IndexError as indexerr:
                print ("No Site Found.")

cursorp = ''
counts = 0
cursortoken = ''
cursorloop = ''
indexCheck = False
print (inputsite)
if os.path.isfile("16INQXE5TJOIQFGZLDOVZGS5DZ.csv"):
        os.remove("16INQXE5TJOIQFGZLDOVZGS5DZ.csv")
if os.path.isfile("18JRGEYTCMJRCUKRKFIVJFEUSS.csv"):
        os.remove("18JRGEYTCMJRCUKRKFIVJFEUSS.csv")
while True:
        
        cursorloop = {"cursor":cursortoken}
        myUrl= 'https://'+inputconsole+'.myurl.net/web/api/v2.0/exclusions?skipCount=false&countOnly=false&limit=100&siteIds='+site_id+'&type=path'
        myUrl2 = 'https://'+inputconsole+'.myurl.net/web/api/v2.0/exclusions?skipCount=false&countOnly=false&limit=100&siteIds='+site_id+'&type=white_hash'
        head = {'Authorization': 'ApiToken {}'.format(inputkey)}
       # print (myUrl2)
        

        response = requests.get(myUrl, headers=head)
        response2 = requests.get(myUrl2, headers=head, params=cursorloop)
        if not response.json()['pagination']['totalItems'] == '0':
                indexCheck = True
        cursortoken = str(response2.json()['pagination']['nextCursor'])
        #print (cursortoken)
        #print (str(response.json()))
        if not str(response2.json()['pagination']['nextCursor']) == 'None':
                
                
              ##TODO Fix this.
                cursorloop = {'cursor':cursortoken}
                
                #print (cursorloop)
       
       
                

        f= open('16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json', 'w')
        data = str(response.json())
        data1 = response.json()
        f.write(json.dumps(data1))
       # print (json.dumps(data1))
        f.close()
        fh = open('17ONVWU3DENRZHK2TENNSGW4TL.json', 'w')
        fhdata = response2.json()

        fh.write(json.dumps(fhdata))

        fh.close()


        f2 = open ('16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json')
        data2 = json.load(f2)
        f2.close()
        datawrite = data2['data']

        f3 = open('16INQXE5TJOIQFGZLDOVZGS5DZ.csv', 'a')
        csvwriter = csv.writer(f3, delimiter =',')
        liste={}
        t = str('file')
        f = str('FALSE')
        end = ''
        for item in datawrite:
                if counts == 0:
                        header = '','abcdef','bacdef','cabdef','dabcef','eabcdf','fabcde'
                        csvwriter.writerow(header)
                        counts += 1
                
                if item['pathExclusionType'] == 'file':
                        t = str('file')
                elif item['pathExclusionType'] == 'folder':
                        t = str('folder')
                elif item['pathExclusionType'] == 'subfolders':
                        t = str('folder')
                liste['first']= t
                liste['osType'] = item['osType']
                liste['value'] = item['value']
                liste['description'] = item['description']

                liste['mode'] = item['mode']
                if item['pathExclusionType'] == 'subfolders':
                        f = str('TRUE')
                        
                liste['pathExclusionType1'] = f
                liste ['addone'] = end
                
                csvwriter.writerow(liste.values())
        f3.close()
        f5 = open ('17ONVWU3DENRZHK2TENNSGW4TL.json')
        data2 = json.load(f5)
       # print (str(data2))
        f5.close()
        datawrite2 = data2['data']
        f6 = open('16INQXE5TJOIQFGZLDOVZGS5DZ.csv', 'a')
        csvwriter = csv.writer(f6, delimiter =',')
        count = 0
        liste1 = {}
        test = str('N/A')

        for item1 in datawrite2:
                liste1['type']= item1['type']
                liste1['osType'] = item1['osType']
                liste1['value'] = item1['value']
                liste1['description'] = item1['description']
                liste1['mode'] = test
                liste1['pathExclusionType'] = test
                
                csvwriter.writerow(liste1.values())
        f6.close()
        if cursortoken == 'None':
                break
df = pd.read_csv('16INQXE5TJOIQFGZLDOVZGS5DZ.csv')

df.to_csv('18JRGEYTCMJRCUKRKFIVJFEUSS.csv', index=False, header=True, encoding='utf-8')

##
##
##
##

##
##
##
def create_file_folder(file_folder):
    
    if file_folder[1] == "osx":
        tmp = "macos"
    else:
        tmp = file_folder[1]
    if file_folder[0] == "file":
        data = {
            "filter": {
                "siteIds": [
                    outsite_id
                ],
                "tenant": True
            },
        "data": {
            "description": file_folder[3],
            "value": file_folder[2],
            "pathExclusionType": file_folder[0],
            "osType": tmp,
            "mode": file_folder[4],
            "type": "path",
            "includeSubfolders" : "false"
        }
        }
    else:
        if (file_folder[5].lower()) == "true":
            pathExclusionType2 = "subfolders"
            data = {
                "filter": {
                    "siteIds": [
                        outsite_id
                        
                    ],
                    "tenant": True
                },
            "data": {
            "description": file_folder[3],
            "value": file_folder[2],
            "pathExclusionType": pathExclusionType2,
            "osType": tmp,
            "mode": file_folder[4],
            "type": "path"
            }
        }
        elif (file_folder[5].lower()) == "false":
            data = {
                "filter": {
                    "siteIds": [
                        outsite_id
                    ],
                    "tenant": True
                },
                "data": {
                    "description": file_folder[3],
                    "value": file_folder[2],
                    "pathExclusionType": "folder",
                    "osType": tmp,
                    "mode": file_folder[4],
                    "type": "path",
                    "includeSubfolders": "false"
                }
            }
    r = requests.post('https://'+outputconsole+'.myurl.net/web/api/v2.0/exclusions', headers=headAUTHOUT, data=json.dumps(data))
    if r.status_code != 200:
        print (("Error: %s") % r.json())
        return False
    return True
            ##
            ##
            ##
def create_white_hash(white_list):
    """This will create a white list exclusions.
    Needed values:
    type = white_hash
    osType - windows, macos , linux  note- osx is also applicable.
    Value - hash ( SHA1 )
    Description  - Put desired description"""
    if white_list[1] == "osx":
        tmp = "macos"
    else:
        tmp = white_list[1]
    data = {
        "filter": {
        "siteIds": [
            outsite_id
        ],
        "tenant": True
        },
    "data": {
        "description": white_list[3],
        "value": white_list[2],
        "osType": tmp,
        "type": "white_hash"
        }
    }
    r = requests.post('https://'+outputconsole+'.myurl.net/web/api/v2.0/exclusions', headers=headAUTHOUT, data=json.dumps(data))
    if r.status_code != 200:
        print (("Error: %s") % r.json())
        print (str(data))
        return False
    return True


def main():
    white_list_success = 0
    white_list_fail = 0
    white_list = []

    file_folder_success = 0
    file_folder_fail = 0
    file_folders_list = []

    certificate_success = 0
    certificate_fail = 0
    certificates_list = []

    file_type_success = 0
    file_type_fail = 0
    file_types_list = []

    fail_list = []

    site_id1 = outsite_id
    csvfile = str('18JRGEYTCMJRCUKRKFIVJFEUSS.csv')
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            if row[0] == "white_hash":
                white_list.append(row)
            elif row[0] == "file":
                file_folders_list.append(row)
            elif row[0] == "folder":
                file_folders_list.append(row)
            elif row[0] == "certificate":
                certificates_list.append(row)
            elif row[0] == "file_type":
                file_types_list.append(row)
            else:
                fail_list.append(row)

    print ("Creating hash exclusion for "+ro.json()['data']['sites'][0]['name']+".")
    for hash in white_list:
        if create_white_hash(hash):
            white_list_success += 1
        else:
            white_list_fail += 1
    print ("Transfer hash exclusion for "+ro.json()['data']['sites'][0]['name']+" has been completed. {} good requests. {} Bad requests".format(white_list_success,
                                                                                                   white_list_fail,
                                                                                                   white_list_success + white_list_fail))

    print ("Creating path exclusion for "+ro.json()['data']['sites'][0]['name']+" .")
    for file_folder in file_folders_list:
        if create_file_folder(file_folder):
            file_folder_success += 1
        else:
            file_folder_fail += 1
    print (
        "Transfer path exclusion for "+ro.json()['data']['sites'][0]['name']+" has been completed. {} good requests. {} bad requests".format(file_folder_success,
                                                                                                  file_folder_fail,
                                                                                                  file_folder_success + file_folder_fail))

    

    
    return
main()


group_parout = {'siteIds': site_id}
so = requests.get('https://'+inputconsole+'.myurl.net/web/api/v2.0/groups?skipCount=false&countOnly=false&limit=200&type=static', headers=headAUTH, params=group_parout)


#print (so.json())
if not so.json()['pagination']['totalItems'] == '0':
        #print ('\n There are currently '+int(so.json()['pagination']['totalItems'])+' groups in your site. \n')
        frgroup= open('13K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json', 'w')
        datagroup = so.json()
        frgroup.write(json.dumps(datagroup))
        #print (json.dumps(datagroup))
        print ("\n\nGetting Groups.....\n\n")
        frgroup.close()
        f3 = open ('13K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json')
        data3 = json.load(f3)
        f3.close()
        groupwrite = data3['data']
        #fgroup = open ('grouplistdprok3409idkf3.csv', 'w')
        #csvwriter = csv.writer(fgroup, delimiter =',')
        groupliste = {}
        grouplistedefault = {}
        
        if os.path.isfile("14K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.csv"):
                os.remove("14K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.csv")
        for item2 in groupwrite:
                if os.path.isfile("16INQXE5TJOIQFGZLDOVZGS5DZ.csv"):
                        os.remove("16INQXE5TJOIQFGZLDOVZGS5DZ.csv")
                if os.path.isfile("18JRGEYTCMJRCUKRKFIVJFEUSS.csv"):
                        os.remove("18JRGEYTCMJRCUKRKFIVJFEUSS.csv")
                groupliste['name']= item2['name']
               # print ('test')
                if "[\"" in str(groupliste.values()):
                        gnr=re.findall('\[\"([^]]+)\"\]', str(groupliste.values()))
                        gn = (gnr[0])
                else:
                        gnr=re.findall('\[\'([^]]+)\'\]', str(groupliste.values()))
                        gn = (gnr[0])
                #print (groupliste.values())
               # print ('test')
                grouplistedefault['id'] = item2['id']
                gnl=re.findall('\'(.+?)\'', str(grouplistedefault.values()))
                gln = (gnl[0])
                #print (gln)
                policy_parout = { 'groupIds': groupliste.values()}
                policypull = requests.get('https://'+inputconsole+'.myurl.net/web/api/v2.0/private/policy', headers=headAUTH, params=policy_parout)
                
## TODO Create Dynamic Group and get filters from other site.
            
                data = {
                    "data": {
                        "inherits": True,
                        "name": gn,
                        "siteId":outsite_id,
                        "isDefault": True
                        
                }
                    }
                        
                
                if not gn == "Defaut Group":
                        r = requests.post('https://'+outputconsole+'.myurl.net/web/api/v2.0/groups', headers=headAUTHOUT, data=json.dumps(data))
                        if r.status_code != 200:
                                print (("Error: %s") % r.json())
                        params = {"siteIds": outsite_id,"name": gn}  
                        rg = requests.get('https://'+outputconsole+'.myurl.net/web/api/v2.0/groups', headers=headAUTHOUT, params=params)
                        if rg.status_code == 200:
                                
                                glno = rg.json()['data'][0]['id']
                                #print (glno)
                                print ("Creating group, "+gn+".")
                                
                cursortoken = ''
                policy_paroutw = { 'groupIds': gln}
                policy_paroutw1 = { 'groupIds': gln}
                gcounts = 0
                while True:
                        
        #cursorloop = {"cursor":cursortoken}
                        myUrl= 'https://'+inputconsole+'.myurl.net/web/api/v2.0/exclusions?skipCount=false&countOnly=false&limit=100&type=path'
                        myUrl2 = 'https://'+inputconsole+'.myurl.net/web/api/v2.0/exclusions?skipCount=false&countOnly=false&limit=100&type=white_hash'
                        head = {'Authorization': 'ApiToken {}'.format(inputkey)}
                        

                        response = requests.get(myUrl, headers=head, params=policy_paroutw)
                        response2 = requests.get(myUrl2, headers=head, params=policy_paroutw1)
                      
                        
                        if response.json()['pagination']['totalItems'] == '0':
                                if response2.json()['pagination']['totalItems'] == '0':
                                        print ("No exclusions for" + gn +"." )
                                        break
                        cursortoken = str(response2.json()['pagination']['nextCursor'])
                        #print (cursortoken)
                       # print (str(response.json()))
                        if not str(response2.json()['pagination']['nextCursor']) == 'None':
                                
                                #cursorloop = {'cursor':cursortoken}
                                policy_paroutw1 = { 'groupIds': gln, "cursor":cursortoken}
                                #print (cursorloop)
                       
                       
                                

                        f= open('16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json', 'w')
                        data = str(response.json())
                        data1 = response.json()
                        f.write(json.dumps(data1))
                        f.close()
                        fh = open('17ONVWU3DENRZHK2TENNSGW4TL.json', 'w')
                        fhdata = response2.json()

                        fh.write(json.dumps(fhdata))

                        fh.close()


                        f2 = open ('16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json')
                        data2 = json.load(f2)
                        f2.close()
                        datawrite = data2['data']

                        f3 = open('16INQXE5TJOIQFGZLDOVZGS5DZ.csv', 'a')
                        csvwriter = csv.writer(f3, delimiter =',')
                        liste={}
                        t = str('file')
                       
                        end = ''
                        for item in datawrite:
                                f = str('FALSE')
                                if gcounts == 0:
                                        header = '','abcdef','bacdef','cabdef','dabcef','eabcdf','fabcde'
                                        csvwriter.writerow(header)
                                        gcounts += 1
                                
                                if item['pathExclusionType'] == 'file':
                                        t = str('file')
                                elif item['pathExclusionType'] == 'folder':
                                        t = str('folder')
                                elif item['pathExclusionType'] == 'subfolders':
                                        t = str('folder')
                                liste['first']= t
                                liste['osType'] = item['osType']
                                liste['value'] = item['value']
                                liste['description'] = item['description']

                                liste['mode'] = item['mode']
                                if item['pathExclusionType'] == 'subfolders':
                                        f = str('TRUE')
                                        
                                liste['pathExclusionType1'] = f
                                liste ['addone'] = end
                                
                                csvwriter.writerow(liste.values())
                        f3.close()
                        f5 = open ('17ONVWU3DENRZHK2TENNSGW4TL.json')
                        data2 = json.load(f5)
                       # print (str(data2))
                        f5.close()
                        datawrite2 = data2['data']
                        f6 = open('16INQXE5TJOIQFGZLDOVZGS5DZ.csv', 'a')
                        csvwriter = csv.writer(f6, delimiter =',')
                        count = 0
                        liste1 = {}
                        test = str('N/A')

                        for item1 in datawrite2:
                                liste1['type']= item1['type']
                                liste1['osType'] = item1['osType']
                                liste1['value'] = item1['value']
                                liste1['description'] = item1['description']
                                liste1['mode'] = test
                                liste1['pathExclusionType'] = test
                                
                                csvwriter.writerow(liste1.values())
                        f6.close()
                        if cursortoken == 'None':
                                break
                if not os.stat('16INQXE5TJOIQFGZLDOVZGS5DZ.csv').st_size == 0:
                      
                        df = pd.read_csv('16INQXE5TJOIQFGZLDOVZGS5DZ.csv')
                        df.to_csv('18JRGEYTCMJRCUKRKFIVJFEUSS.csv', index=False, header=True, encoding='utf-8')
                        def create_file_folder1(file_folder):
                            
                            if file_folder[1] == "osx":
                                tmp = "macos"
                            else:
                                tmp = file_folder[1]
                            if file_folder[0] == "file":
                                data = {
                                    "filter": {
                                        "groupIds":[
                                                glno
                                        ],
                                        "tenant": True
                                    },
                                "data": {
                                    "description": file_folder[3],
                                    "value": file_folder[2],
                                    "pathExclusionType": file_folder[0],
                                    "osType": tmp,
                                    "mode": file_folder[4],
                                    "type": "path",
                                    "includeSubfolders" : "false"
                                }
                                }
                            else:
                                if (file_folder[5].lower()) == "true":
                                    pathExclusionType3 = "subfolders"
                                    data = {
                                        "filter": {
                                            "groupIds":[
                                                glno
                                        ],
                                            "tenant": True
                                        },
                                    "data": {
                                    "description": file_folder[3],
                                    "value": file_folder[2],
                                    "pathExclusionType": pathExclusionType3,
                                    "osType": tmp,
                                    "mode": file_folder[4],
                                    "type": "path"
                                    }
                                }
                                elif (file_folder[5].lower()) == "false":
                                    data = {
                                        "filter": {
                                            "groupIds":[
                                                glno
                                        ],
                                            "tenant": True
                                        },
                                        "data": {
                                            "description": file_folder[3],
                                            "value": file_folder[2],
                                            "pathExclusionType": "folder",
                                            "osType": tmp,
                                            "mode": file_folder[4],
                                            "type": "path",
                                            "includeSubfolders": "false"
                                        }
                                    }
                            r = requests.post('https://'+outputconsole+'.myurl.net/web/api/v2.0/exclusions', headers=headAUTHOUT, data=json.dumps(data))
                            if r.status_code != 200:
                                print (("Error: %s") % r.json())
                                return False
                            return True
                                    ##
                                    ##
                                    ##
                        def create_white_hash1(white_list):
                            """This will create a white list exclusions.
                            Needed values:
                            type = white_hash
                            osType - windows, macos , linux  note- osx is also applicable.
                            Value - hash ( SHA1 )
                            Description  - Put desired description"""
                            if white_list[1] == "osx":
                                tmp = "macos"
                            else:
                                tmp = white_list[1]
                            data = {
                                "filter": {
                                "groupIds": [
                                    glno
                                ],

                                "tenant": True
                                },
                            "data": {
                                "description": white_list[3],
                                "value": white_list[2],
                                "osType": tmp,
                                "type": "white_hash"
                                }
                            }
                            r = requests.post('https://'+outputconsole+'.myurl.net/web/api/v2.0/exclusions', headers=headAUTHOUT, data=json.dumps(data))
                            if r.status_code != 200:
                                print (("Error: %s") % r.json())
                                return False
                            return True


                        def main1():
                            white_list_success = 0
                            white_list_fail = 0
                            white_list = []

                            file_folder_success = 0
                            file_folder_fail = 0
                            file_folders_list = []

                            certificate_success = 0
                            certificate_fail = 0
                            certificates_list = []

                            file_type_success = 0
                            file_type_fail = 0
                            file_types_list = []

                            fail_list = []

                            site_id1 = outsite_id
                            csvfile = str('18JRGEYTCMJRCUKRKFIVJFEUSS.csv')
                            with open(csvfile) as csv_file:
                                csv_reader = csv.reader(csv_file, delimiter=',')
                                line_count = 0
                                for row in csv_reader:
                                    line_count += 1
                                    if line_count == 1:
                                        continue
                                    if row[0] == "white_hash":
                                        white_list.append(row)
                                    elif row[0] == "file":
                                        file_folders_list.append(row)
                                    elif row[0] == "folder":
                                        file_folders_list.append(row)
                                    elif row[0] == "certificate":
                                        certificates_list.append(row)
                                    elif row[0] == "file_type":
                                        file_types_list.append(row)
                                    else:
                                        fail_list.append(row)

                            print ("Creating Hash exclusion for " +gn+".")
                            for hash in white_list:
                                if create_white_hash1(hash):
                                    white_list_success += 1
                                else:
                                    white_list_fail += 1
                            print ("Creating hash exclusion for "+gn+". {} good requests. {} bad requests.".format(white_list_success,
                                                                                                                           white_list_fail,
                                                                                                                           white_list_success + white_list_fail))

                            print ("Creating Path exclusion for "+gn+".")
                            for file_folder in file_folders_list:
                                if create_file_folder1(file_folder):
                                    file_folder_success += 1
                                else:
                                    file_folder_fail += 1
                            print (
                                "Creating path exclusion for "+gn+". {} good requests. {} bad requests.".format(file_folder_success,
                                                                                                                          file_folder_fail,
                                                                                                                          file_folder_success + file_folder_fail))

                           
                            

                            
                            return
                        main1()

                
if os.path.isfile("16INQXE5TJOIQFGZLDOVZGS5DZ.csv"):
        os.remove("16INQXE5TJOIQFGZLDOVZGS5DZ.csv")
if os.path.isfile("18JRGEYTCMJRCUKRKFIVJFEUSS.csv"):
        os.remove("18JRGEYTCMJRCUKRKFIVJFEUSS.csv")
if os.path.isfile("16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json"):
        os.remove("16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json")
if os.path.isfile("17ONVWU3DENRZHK2TENNSGW4TL.json"):
        os.remove("17ONVWU3DENRZHK2TENNSGW4TL.json")
if os.path.isfile("13K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json"):
        os.remove("13K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json")

        
