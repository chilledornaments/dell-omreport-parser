#!/usr/bin/env python36
# ./omreport chassis fans -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_arg = "chassis"
dell_arg_two = "fans"

host = "xenserver"
json_report = {}
json_report['Host'] = host
json_report['Category'] = "Memory"
json_report['Report'] = {}

text_out = subprocess.check_output([dell_tool, dell_arg, dell_arg_two, '-fmt', 'xml']).decode('utf-8')

text_xml = ET.fromstring(text_out)