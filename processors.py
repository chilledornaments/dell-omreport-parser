#!/usr/bin/env python36
# ./omreport chassis processors -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json, post_metrics
from config import *

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_arg = "chassis"
dell_arg_two = "processors"

host = host

text_out = subprocess.check_output([dell_tool, dell_arg, dell_arg_two, '-fmt', 'xml']).decode('utf-8')

text_xml = ET.fromstring(text_out)

json_report = {}
json_report['Host'] = host
json_report['Category'] = "Processors"
json_report['Report'] = {}

for e in text_xml.iter('OMA'):
    for p in e.iter('ProcessorList'):
        for pc in p.iter('ProcessorConn'):
            for d in pc.iter('DevProcessor'):
                proc_name = d.find('ExtName').text
                max_speed = d.find('MaxSpeed').text
                curr_speed = d.find('CurSpeed').text
                # 3 seems to be OK
                status = d.find('ProcessorStatus').text
                manufacturer = d.find('Manufacturer').text
                version = d.find('Version').text
                cores = d.find('CoreCount').text
                thread_count = d.find('ThreadCount').text
                json_ = {"ProcessorName": proc_name, "MaxSpeed": max_speed, "CurrentSpeed": curr_speed, "Status": status, \
                "Manufacturer": manufacturer, "Version": version, "Cores": cores, "Threads": thread_count}
                json_report['Report'][proc_name] = json_
                #json_report['Report'].append({proc_name: json_})
print(json.dumps(json_report))
