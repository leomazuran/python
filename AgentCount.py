import requests
import json
import os
import csv
import certifi
from datetime import datetime, timedelta
import time

console_list = ['console1.cox.com', 'console2.corp.cox.com', 'console3.corp.cox.com']
console_keys = ['console1 api key','console2 key','console2 key']
# Time delta (days) for Workstations
workstation_active_days=10
# Time delta (days) for servers
servers_active_days=10
LinuxCount=0
UbuntuCount=0
RHELCount=0
CentOSCount=0
OtherLinuxCount=0
WindowsCount=0
WindowsWSCount=0
WindowsServerCount=0
MacCount=0
today = datetime.now()
workstation_active = today - timedelta(days=workstation_active_days)
server_active = today - timedelta(days=servers_active_days)
print(workstation_active)
for (console, key) in zip(console_list, console_keys):
    SITEURL = 'https://{}:8443/api/v1/sensor'.format(console)
    headSITE = {'X-Auth-Token':key,'Content-Type': 'application/json'}
    sitecall = requests.get(SITEURL, headers=headSITE)
    if sitecall.ok:
        print('Exporting {} list'.format(console))
    else:
        print (("Error: %s") % sitecall.json())
        exit()
    sensor_save = open('{}.json'.format(console), 'w')
    save = sitecall.json()
    sensor_save.write(json.dumps(save))
    sensor_save.close()

for console in console_list:
    sensor_read = open('{}.json'.format(console))
    get_data = json.load(sensor_read)
    sensor_read.close()
    for item in get_data:
        

    
   
   
   
        if item['os_type'] ==1:
            WindowsCount+=1

            if 'Windows Server' in item['os_environment_display_string'] and item['last_checkin_time'] >= str(server_active):
                    WindowsServerCount+=1
            elif item['last_checkin_time'] >= str(workstation_active):
                WindowsWSCount+=1
        # Linux 
        if item['os_type']==3 and item['last_checkin_time'] >= str(server_active) :
            LinuxCount+=1
            if 'Red Hat' in item['os_environment_display_string']:
                RHELCount+=1
            elif 'Ubuntu' in item['os_environment_display_string']:
                UbuntuCount+=1
            elif 'CentOS' in item['os_environment_display_string']:
                CentOSCount+=1
            else:
                OtherLinuxCount+=1

        # Mac
        if item['os_type']==2 and item['last_checkin_time'] >= str(workstation_active):
            MacCount+=1
        
# Windows Output
print('Total Windows Count: {}'.format(WindowsCount) )
print('Total Windows Workstation Count: {}'.format(WindowsWSCount) )
print('Total Windows Server Count: {}'.format(WindowsServerCount) )
    
# Linux Output
print('Total Linux Count: {}'.format(LinuxCount) )
print('Total Linux RHEL Count: {}'.format(RHELCount) )
print('Total Linux Ubuntu Count: {}'.format(UbuntuCount) )
print('Total Linux CentOS Count: {}'.format(CentOSCount) )
print('Total Linux Other Count: {}'.format(OtherLinuxCount) )
# Mac
print('Total MacOS Count: {}'.format(MacCount) )
# Total
print('Overall Total Count: {}'.format(WindowsCount+LinuxCount+MacCount))
