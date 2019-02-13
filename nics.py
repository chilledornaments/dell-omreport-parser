#!/usr/bin/env python36
# ./omreport chassis nics -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json, post_metrics
from config import *

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_arg = "chassis"
dell_arg_two = "nics"

host = host
json_report = {}
json_report['Host'] = host
json_report['Category'] = "NICs"
json_report['Report'] = {}

text_out = subprocess.check_output([dell_tool, dell_arg, dell_arg_two, '-fmt', 'xml']).decode('utf-8')


text_xml = ET.fromstring(text_out)


for e in text_xml.iter('OMA'):
    for i in e.iter('DevNicObj'):
        name = i.find('IfDescription').text
        desc = i.find('OSAdapterDescription').text
        slot = i.find('SlotName').text
        mtu = i.find('mtu').text
        vendor = i.find('OSAdapterVendor').text
        driver_version = i.find('DriverVersion').text
        fw_version = i.find('FirmwareVersion').text
        curr_mac = i.find('CurrentMACAddr').text
        json_ = {"Name": name, "Description": desc, "Slot": slot, "MTU": mtu, "Vendor": vendor, "DriverVersion": driver_version, "FirmwareVersion": fw_version, "CurrentMAC": curr_mac}
        json_report['Report'][name] = json_
    for v in e.iter('VirNicObj'):
        name = v.find('IfDescription').text
        desc = v.find('OSAdapterDescription').text
        slot = v.find('SlotName').text
        mtu = v.find('mtu').text
        vendor = v.find('OSAdapterVendor').text
        driver_version = v.find('DriverVersion').text
        curr_mac = v.find('CurrentMACAddr').text
        json_ = {"Name": name, "Description": desc, "Slot": slot, "MTU": mtu, "Vendor": vendor, "DriverVersion": "null", "FirmwareVersion": "null", "CurrentMAC": curr_mac}
        json_report['Report'][name] = json_

print(json.dumps(json_report))