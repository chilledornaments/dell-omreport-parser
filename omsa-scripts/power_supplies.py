#!/usr/bin/env python36
# ./omreport chassis pwrsupplies -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json, post_metrics
from config import *

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_arg = "chassis"
dell_arg_two = "pwrsupplies"

host = host

json_report = {}
json_report['Host'] = host
json_report['Category'] = "PowerSupplies"
json_report['Report'] = {}

text_out = subprocess.check_output([dell_tool, dell_arg, dell_arg_two, '-fmt', 'xml']).decode('utf-8')


text_xml = ET.fromstring(text_out)


for e in text_xml.iter('OMA'):
    for i in e.iter('Chassis'):
        for f in i.iter('PowerSupplyList'):
            for r in f.iter('PowerSupply'):
                ac_on = r.find('PSACOn').text
                name = r.find('PSLocation').text
                input_rating = r.find('InputRatedWatts').text
                fan_ok = r.find('PSFanFail').text
                fw_ver = r.find('FirmWareVersion').text
                for p in r.iter('PSState'):
                    exists = p.find('PSPresenceDetected').text
                    failed = p.find('PSFailureDetected').text
                    predict_fail = p.find('PSPredictiveFailure').text
                    ac_status = p.find('PSACLost').text
                json_ = {"Name": name, "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_ok, "FirmwareVersion": fw_ver, "ACOn": ac_on}
                json_report['Report'][name] = json_


post_ = post_metrics.PostMetrics()
r = post_.post(json_)
print(r)