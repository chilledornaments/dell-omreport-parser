#!/usr/bin/env python36
# ./omreport storage pdisk controller=0 -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json, post_metrics
from config import *

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_strg_arg = "storage"
dell_pdisk_arg = "pdisk"
dell_controller_arg = "controller=0"

#host = host
host = "xenserver2"

json_report = {}
json_report['Host'] = host
json_report['Category'] = "PhysicalDisks"
json_report['Report'] = {}

pdisk_out = subprocess.check_output([dell_tool, dell_strg_arg, dell_pdisk_arg, dell_controller_arg, '-fmt', 'xml']).decode('utf-8')

pdisk_xml = ET.fromstring(pdisk_out)

for e in pdisk_xml.iter('OMA'):
    for i in e.iter('ArrayDisks'):
        for d in i.iter('DCStorageObject'):
            oid = d.find('ObjID').text
            serial = d.find('DeviceSerialNumber').text
            num_partitions = d.find('NumOfPartition').text
            neg_speed = d.find('NegotiatedSpeed').text
            capable_speed = d.find('CapableSpeed').text
            product_id = d.find('ProductID').text
            # Presumably 4 is OK
            status = d.find('ObjStatus').text
            json_ = {"ProductID": product_id, "ObjectID": oid, "Serial": serial, "NumPartitions": num_partitions, "NegotiatedSpeed": neg_speed, "CapableSpeed": capable_speed, "Status": status}
            json_report['Report'][oid] = json_
            #json_report['Report'].append({oid: pdisk_json})

post_ = post_metrics.PostMetrics()
r = post_.post(json_)
print(r)