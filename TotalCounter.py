## Author: Leonardo Mazuran


import requests
import json
import re
from tkinter import *
import time
##UserName API Keys**********
myToken_nafcs = ''
myToken_carvir = ''
myToken_msp02 = ''
myToken_bigben = ''
#**** GUI configuratiuon *******
root = Tk()
root.title('Total Counter')
root.geometry("1380x720")

description = StringVar()
description.set('No Calculators Needed!')
number = StringVar()
number.set('LOAD')
l = Label(root, text="Total Number of Agents:",fg="black", font="none 64 bold")
l.place(x= 690, y = 50, anchor='center')
n = Label(root, textvariable=number,fg="black", font="none 300 bold")
n.place(x= 690, y = 350, anchor='center')
# API Calls ####
def run (master):
        try:
                
                auth = True
                #API URL
                myUrl_msp = 'https://myurl.net//web/api/v1.6/agents/count'
                # API Header Information
                head = {'Authorization': 'APIToken {}'.format(myToken_MSP)}
                # get resonse
                response_msp = requests.get(myUrl_msp, headers=head)
                # check response (if 401 is true, return false)
                check1 = str(response_msp)
                a = int(0)
                if check1 == "<Response [401]>":
                        auth = False
                else:     
                        # regex to find numbers and put it in a intergar format. 
                        carvir_msp = re.findall(b'(\\d+)', response_msp.content)
                        a = int(carvir_msp[0])
                # same processes as above.
                myUrl_nafcs = 'https://myurl1.net//web/api/v1.6/agents/count'
                head = {'Authorization': 'APIToken {}'.format(myToken_nafcs)}
                response_nafcs = requests.get(myUrl_nafcs, headers=head)
                check2 = str(response_nafcs)
                b = int(0)
                if check2 == "<Response [401]>":
                        auth = False
                else:
                        carvir_nafcs = re.findall(b'(\\d+)', response_nafcs.content)
                        b = int(carvir_nafcs[0])
                myUrl_carvir = 'https://myurl2.net//web/api/v1.6/agents/count'
                head = {'Authorization': 'APIToken {}'.format(myToken_carvir)}
                response_carvir = requests.get(myUrl_carvir, headers=head)
                check3 = str(response_carvir)
                c = int(0)
                if check3 == "<Response [401]>":
                        auth = False
                else:
                        carvir_carvir = re.findall(b'(\\d+)', response_carvir.content)
                        c = int(carvir_carvir[0])
                myUrl_msp02 = 'https://myurl3.net//web/api/v2.0/agents/count'
                head = {'Authorization': 'ApiToken {}'.format(myToken_msp02)}
                response_msp02 = requests.get(myUrl_msp02, headers=head)
                check4 = str(response_msp02)
                d = int(0)
                if check4 == "<Response [401]>":
                        auth = False
                else:
                        carvir_msp02 = re.findall(b'(\\d+)', response_msp02.content)
                        d = int(carvir_msp02[0])
                myUrl_bigben = 'https://myurl4.net//web/api/v2.0/agents/count'
                head = {'Authorization': 'ApiToken {}'.format(myToken_bigben)}
                response_bigben = requests.get(myUrl_bigben, headers=head)
                check5 = str(response_bigben)
                e = int(0)
                if check5 == "<Response [401]>":
                        auth = False
                else:
                        carvir_bigben = re.findall(b'(\\d+)', response_bigben.content)
                        e = int(carvir_bigben[0])
              
                 # add integers from several sites up.
                n1=a+b+c+d+e
                print (n1)
                # if number reach 500k, give eror of ID10T.
                if n1 > 500000:
                        number.set('ID10T')
               # if one of the site shows to have permissions, display error on gui
                elif auth==False:
                      number.set("E401")
                      description.set('One or More API Tokens Are Revoked/Expired. Please contact Leo.')
                      root.after(10000, run, master)
                else:
                        #display total number of agents.
                        number.set(n1)
                        description.set('No Calculators Needed!')
                root.after(40000, run, master)


        except:
                number.set("FAIL")
                description.set('Attempting To Get Data! ')
                root.after(3000, run, master)
m = Label(root, textvariable=description,fg="black", font="none 32 bold")
m.place(x= 690, y = 600, anchor='center')
m = Label(root, text="Author: Leonardo Mazuran",fg="black", font="none 5 bold")
m.place(x= 1300, y = 700, anchor='center')
run(root)
root.mainloop()
