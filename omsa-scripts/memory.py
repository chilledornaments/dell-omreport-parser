#!/usr/bin/env python36
# ./omreport chassis memory -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json, post_metrics
from config import *

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_arg = "chassis"
dell_mem_arg = "memory"

host = host

mem_out = subprocess.check_output([dell_tool, dell_arg, dell_mem_arg, '-fmt', 'xml']).decode('utf-8')

mem_xml = ET.fromstring(mem_out)

json_report = {}
json_report['Host'] = host
json_report['Category'] = "Memory"
json_report['Report'] = {}


for e in mem_xml.iter('OMA'):
    for i in e.iter('MemDevObj'):
        dev_location = i.find('DeviceLocator').text
        manufacturer = i.find('Manufacturer').text
        serial = i.find('SerialNumber').text
        part_number = i.find('PartNumber').text
        speed = i.find('speed').text
        size = i.find('size').text
        status = i.find('failureModes').text
        json_ = {"Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status}
        json_report['Report'][dev_location] = json_
        #json_report['Report'].append({dev_location: mem_json})
        
post_ = post_metrics.PostMetrics()
r = post_.post(json_)
print(r)


# Presumably, a failureMode of anything besides 0 is bad
# 3 = critical
