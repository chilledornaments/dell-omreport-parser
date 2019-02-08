#!/usr/bin/env python36
import subprocess, requests, json
import xml.etree.ElementTree as ET
from config import *

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_strg_arg = "storage"
dell_arg = "vdisk"

host = host

json_report = {}
json_report['Host'] = host
json_report['Category'] = "VirtDisk"
json_report['Report'] = {}

vdisk_out = subprocess.check_output([dell_tool, dell_strg_arg, dell_arg, '-fmt', 'xml']).decode('utf-8')

vdisk_xml = ET.fromstring(vdisk_out)

for e in vdisk_xml.iter('OMA'):
    for i in e.iter('VirtualDisks'):
        for d in i.iter('DCStorageObject'):
            oid = d.find('ObjID').text
            status = d.find('ObjState').text
            device_name = d.find('DeviceName').text
            pool_name = d.find('Name').text
            stripe_size = d.find('StripeSize').text
            json_ = {"ObjectID": oid, "DeviceName": device_name, "PoolName": pool_name, "Status": status, "StripeSize": stripe_size}
            json_report['Report'][device_name] = json_
            #json_report['Report'].append({device_name: vdisk_json})

print(json.dumps(json_report))