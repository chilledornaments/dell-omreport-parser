#!/usr/bin/env python36
# ./omreport chassis fans -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json, post_metrics
from config import *

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_arg = "chassis"
dell_arg_two = "fans"

host = host
json_report = {}
json_report['Host'] = host
json_report['Category'] = "Fans"
json_report['Report'] = {}

text_out = subprocess.check_output([dell_tool, dell_arg, dell_arg_two, '-fmt', 'xml']).decode('utf-8')

text_xml = ET.fromstring(text_out)

for e in text_xml.iter('OMA'):
    for i in e.iter('Chassis'):
        for f in i.iter('FanProbeList'):
            for r in f.iter('FanProbe'):
                dev_name = r.find('ProbeLocation').text
                speed = r.find('ProbeReading').text
                json_ = {"DeviceName": dev_name, "SpeedInRPM": speed}
                json_report['Report'][dev_name] = json_

post_ = post_metrics.PostMetrics()
r = post_.post(json_report)
print(r)

