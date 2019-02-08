#!/usr/bin/env python36
# ./omreport chassis fans -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_arg = "chassis"
dell_arg_two = "temps"

host = "xenserver"
json_report = {}
json_report['Host'] = host
json_report['Category'] = "Temperature"
json_report['Report'] = {}

text_out = subprocess.check_output([dell_tool, dell_arg, dell_arg_two, '-fmt', 'xml']).decode('utf-8')


text_xml = ET.fromstring(text_out)


for e in text_xml.iter('OMA'):
    for i in e.iter('Chassis'):
        for f in i.iter('TemperatureProbeList'):
            for r in f.iter('TemperatureProbe'):
                # It seems that the current temp in Celsius is this reading with the decimal moved to the left one space
                temp = r.find('ProbeReading').text
                name = r.find('ProbeLocation').text
                json_ = {"TempReading": name, "TempInC": temp}
                #print(json_)
                json_report['Report'][name] = json_


print(json.dumps(json_report))