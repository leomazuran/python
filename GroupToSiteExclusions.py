import requests
import time
import json
import os
import csv
import re
import pandas as pd
valid_character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=-'
def clear(x):
    import os
    time.sleep(x)
    os.system('cls')
def Console_URL():
    while (True):
        try:
            inputchoice = ""
            print ("Please select a Console\n\n")
            print ("1. Carvir-MSP\n")
            print ("2. Carvir-MSP02\n")
            print ("3. Carvir-Bigben\n")

            inputchoice = input (' 1-3: ')
            if inputchoice == "1":
                console = "carvir-msp"
                return console
                break
            elif inputchoice == "2":
                console = "carvir-msp02"
                return console
                break
            elif inputchoice == "3":
                console = "carvir-bigben"
                return console
                break
            else:
                print ("Invalid Input")
        except:
            print ("\nSomething went wrong. Please try again")



def API_Key (Console_ask_get):
    while True:


        inputkey = input('Key: ')

        if all(char in valid_character for char in inputkey):
            AUTHURL = 'https://' + Console_ask_get + '.sentinelone.net/web/api/v2.0/private/user-info'
            headAUTH = {'Authorization': 'ApiToken {}'.format(inputkey)}
            authcheck = requests.get(AUTHURL, headers=headAUTH)
            print('Checking key')
            if str(authcheck) == "<Response [401]>":
                print('Key is not valid for Console.')
            elif str(authcheck) == "<Response [200]>":
                print("\n\nKey is valid. \n")
                if not authcheck.json()['data']['role'] == 'admin':
                    print("However, you are not a Global Administrator.\n\n\n\n")
                    time.sleep(3)
                    print("GoodBye!!!!")
                    time.sleep(2)
                    exit(1)
                elif authcheck.json()['data']['role'] == 'admin':
                    print ("Good")
                    return inputkey
                    break

            else:
                print("Please Try Again.")
def Get_site(Console,key):
    while True:
        inputSite = input("Source Site Name:" )
        if all(char in valid_character for char in inputSite):
            SITEURL = 'https://' + Console + '.sentinelone.net/web/api/v2.0/sites?skipCount=false&query='+inputSite+'&state=active&countOnly=false&limit=100'
            headSITE = {'Authorization': 'ApiToken {}'.format(key), 'Content-type': 'application/json', 'Accept':'text/plain'}
            sitecheck = requests.get(SITEURL, headers=headSITE)
            print ('Getting Sites')

            if str(sitecheck) == "<Response [401]>":
                print('Unable to get sites for  ' + Console + '.')
            elif str(sitecheck) == "<Response [200]>":
                print("\n\n\n")
                if sitecheck.json()['pagination']['totalItems'] > 0:
                    site_name_1 = sitecheck.json()['data']['sites'][0]['name']
                    site_id_1 = sitecheck.json()['data']['sites'][0]['id']
                    site_name = "Site Name: "+sitecheck.json()['data']['sites'][0]['name']
                    site_id = " Site ID: "+sitecheck.json()['data']['sites'][0]['id']
                    print (site_name,site_id)

                    choose = input ("Correct ? ['y', 'n', 'q']")
                    choose1 = choose[0].lower()

                    if choose1 == 'y':
                        site_idn = site_name_1.split("-")[0]
                        return site_idn,site_id_1
                        break
                    if choose1 =='n':
                        clear(1)
                    if choose1 == 'q':
                        exit(1)



                elif sitecheck.json()['pagination']['totalItems'] <= 0:
                    print ("No Sites Found")


            else:
                print("Please Try Again.")



def create_file_folder(file_folder, outsite_id, outputconsole, inputkey):
    headAUTHOUT = {'Authorization': 'ApiToken {}'.format(inputkey), 'Content-type': 'application/json', 'Accept':'text/plain'}
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
                "includeSubfolders": "false"
            }
        }
    else:
        if (file_folder[5].lower()) == "true":
            pathExclusionType = "subfolders"
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
                    "pathExclusionType": pathExclusionType,
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
    r = requests.post('https://' + outputconsole + '.sentinelone.net/web/api/v2.0/exclusions', headers=headAUTHOUT,
                      data=json.dumps(data))
    if r.status_code != 200:
        print(("Error: %s") % r.json())
        print (data)
        return False
    return True
    ##
    ##
    ##


def create_white_hash(white_list, outsite, outputConsole, inputkey):
    headAUTHOUT = {'Authorization': 'ApiToken {}'.format(inputkey), 'Content-type': 'application/json',
                   'Accept': 'text/plain'}
    if white_list[1] == "osx":
        tmp = "macos"
    else:
        tmp = white_list[1]
    data = {
        "filter": {
            "siteIds": [
                outsite
            ],
            "tenant": "true"
        },
        "data": {
            "description": white_list[3],
            "value": white_list[2],
            "osType": tmp,
            "type": "white_hash"
        }
    }
    r = requests.post('https://' +outputConsole + '.sentinelone.net/web/api/v2.0/exclusions', headers=headAUTHOUT,
                      data=json.dumps(data))
    if r.status_code != 200:
        print(("Error: %s") % r.json())
        print(str(data))
        return False
    return True


def main( site_id,Console_ask, inputcode):
    print ( site_id, Console_ask, inputcode)
    getcsv = "18JRGEYTCMJRCUKRKFIVJFEUSS.csv"
    outsite_id = site_id
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
    csvfile = str(getcsv)
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

    print("Creating hash exclusion")
    for hash in white_list:
        if create_white_hash(hash,outsite_id, Console_ask, inputcode):
            white_list_success += 1
        else:
            white_list_fail += 1
    print("Transfer hash exclusion for has been completed. {} good requests. {} Bad requests".format(white_list_success,
                                                                                  white_list_fail,
                                                                                  white_list_success + white_list_fail))

    print("Creating path exclusion for")
    for file_folder in file_folders_list:
        if create_file_folder(file_folder, outsite_id, Console_ask, inputcode):
            file_folder_success += 1
        else:
            file_folder_fail += 1
    print(
        "Transfer path exclusion for has been completed. {} good requests. {} bad requests".format(file_folder_success,
                                                                                      file_folder_fail,
                                                                                      file_folder_success + file_folder_fail))

    return
def New_Site (site_id,key,Console,source_name):
    while True:

            SITEURL = 'https://' + Console + '.sentinelone.net/web/api/v2.0/groups?skipCount=false&siteIds='+site_id+'&countOnly=false&limit=200'
            print (SITEURL)
            headSITE = {'Authorization': 'ApiToken {}'.format(key),'Content-type': 'application/json', 'Accept':'text/plain'}
            sitecheck = requests.get(SITEURL, headers=headSITE)
            print ('Getting Sites')
            if str(sitecheck) == "<Response [401]>":
                print('Unable to get groups for  ' + Console + '.')
            elif str(sitecheck) == "<Response [200]>":
                print("\n\n \n")
                if sitecheck.json()['pagination']['totalItems'] > 0:
                   sitecount = sitecheck.json()['pagination']['totalItems']
                   print ("Group Count" ,sitecount)
                   site_list = []
                   site_name = []
                   count = 0

                   for x in range (0,sitecount):
                       if sitecheck.json()['data'][x]['name'] == "Default Group":
                           print ("****Default group not added")
                       else:
                        print (sitecheck.json()['data'][x]['name'])
                        site_name.append(sitecheck.json()['data'][x]['name'])
                        site_list.append(sitecheck.json()['data'][x]['id'])
                   choose = input("Correct? ['y','q']")
                   choose1 = choose[0].lower()
                   if choose1 == 'y':

                        break
                   if choose1 == 'q':
                       exit(1)
                elif sitecheck.json()['pagination']['totalItems'] <= 0:
                    print ("No Sites Found")



            else:
                print("Please Try Again.")


    for glist,gname in zip(site_list,site_name):
        print (glist,gname)
        if os.path.isfile("16INQXE5TJOIQFGZLDOVZGS5DZ.csv"):
            os.remove("16INQXE5TJOIQFGZLDOVZGS5DZ.csv")
        if os.path.isfile("18JRGEYTCMJRCUKRKFIVJFEUSS.csv"):
            os.remove("18JRGEYTCMJRCUKRKFIVJFEUSS.csv")


        policy_parout = {'groupIds': site_list}
        policypull = requests.get('https://' + Console + '.sentinelone.net/web/api/v2.0/private/policy',
                                  headers=headSITE, params=policy_parout)

        if Console == 'carvir-msp':
            aid = 426438926979301378
        elif Console == 'carvir-msp02':
            aid = 436536346778198719
        elif Console == 'carvir-bigben':
            aid = 426426576751878026

        inputname = ''.join((source_name,'-',gname))

        data ={
  "data": {
    "totalLicenses": 0,
    "unlimitedExpiration": True,
    "inherits": True,
    "unlimitedLicenses": True,
    "accountId": aid,
    "name": inputname,
    "sku": "Core",
    "suite": "Core"
  }
}
        print (json.dumps(data))
        r = requests.post('https://' + Console + '.sentinelone.net/web/api/v2.0/sites',
                            headers=headSITE, data=json.dumps(data))
        if r.status_code != 200:
            print(("Error: %s") % r.json())
        params = {"name": inputname}
        rg = requests.get('https://' + Console + '.sentinelone.net/web/api/v2.0/sites?',
                            headers=headSITE, params=params)
        if rg.status_code == 200:
            glno = rg.json()['data']['sites'][0]['id']
            # print (glno)
            print("Creating site, " + inputname + ".")

        cursortoken = ''
        policy_paroutw = {'siteIds': glist}
        policy_paroutw1 = {'siteIds': glist}
        gcounts = 0
        while True:

            myUrl = 'https://' + Console + '.sentinelone.net/web/api/v2.0/exclusions?skipCount=false&countOnly=false&limit=100&type=path'
            myUrl2 = 'https://' + Console + '.sentinelone.net/web/api/v2.0/exclusions?skipCount=false&countOnly=false&limit=100&type=white_hash'
            head = {'Authorization': 'ApiToken {}'.format(key)}

            response = requests.get(myUrl, headers=head, params=policy_paroutw)
            response2 = requests.get(myUrl2, headers=head, params=policy_paroutw1)

            if response.json()['pagination']['totalItems'] == '0':
                if response2.json()['pagination']['totalItems'] == '0':
                    print("No exclusions for" + input_ + ".")
                    break
            cursortoken = str(response2.json()['pagination']['nextCursor'])
            # print (cursortoken)
            # print (str(response.json()))
            if not str(response2.json()['pagination']['nextCursor']) == 'None':
                # cursorloop = {'cursor':cursortoken}
                policy_paroutw1 = {'siteIds': site_id, "cursor": cursortoken}
                # print (cursorloop)

            f = open('16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json', 'w')
            data = str(response.json())
            data1 = response.json()
            f.write(json.dumps(data1))
            f.close()
            fh = open('17ONVWU3DENRZHK2TENNSGW4TL.json', 'w')
            fhdata = response2.json()

            fh.write(json.dumps(fhdata))

            fh.close()

            f2 = open('16K5UGC5DZN52XEZDVOJUW4Z3UNBSWK4TF.json')
            data2 = json.load(f2)
            f2.close()
            datawrite = data2['data']

            f3 = open('16INQXE5TJOIQFGZLDOVZGS5DZ.csv', 'a', encoding='utf-8')
            csvwriter = csv.writer(f3, delimiter=',')
            liste = {}
            t = str('file')

            end = ''
            for item in datawrite:
                f = str('FALSE')
                if gcounts == 0:
                    header = '', 'abcdef', 'bacdef', 'cabdef', 'dabcef', 'eabcdf', 'fabcde'
                    csvwriter.writerow(header)
                    gcounts += 1

                if item['pathExclusionType'] == 'file':
                    t = str('file')
                elif item['pathExclusionType'] == 'folder':
                    t = str('folder')
                elif item['pathExclusionType'] == 'subfolders':
                    t = str('folder')
                liste['first'] = t
                liste['osType'] = item['osType']
                liste['value'] = item['value']
                liste['description'] = item['description']

                liste['mode'] = item['mode']
                if item['pathExclusionType'] == 'subfolders':
                    f = str('TRUE')

                liste['pathExclusionType1'] = f
                liste['addone'] = end

                csvwriter.writerow(liste.values())
            f3.close()
            f5 = open('17ONVWU3DENRZHK2TENNSGW4TL.json')
            data2 = json.load(f5)
            # print (str(data2))
            f5.close()
            datawrite2 = data2['data']
            f6 = open('16INQXE5TJOIQFGZLDOVZGS5DZ.csv', 'a')
            csvwriter = csv.writer(f6, delimiter=',')
            count = 0
            liste1 = {}
            test = str('N/A')

            for item1 in datawrite2:
                liste1['type'] = item1['type']
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
            main( glno, Console, key)




GetConsole = Console_URL()
Console_ask = GetConsole

inputcode = API_Key(Console_ask)
clear(1)
source_site,source_idn = Get_site(Console_ask,inputcode)
clear(1)
New_Site(source_idn,inputcode,Console_ask,source_site)
