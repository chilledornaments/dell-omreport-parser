#!/usr/bin/env python36
import subprocess, requests, json
import xml.etree.ElementTree as ET


dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_strg_arg = "storage"
dell_controller_arg = "controller"

host = "xenserver"


controller_out = subprocess.check_output([dell_tool, dell_strg_arg, dell_controller_arg, '-fmt', 'xml']).decode('utf-8')

controller_xml = ET.fromstring(controller_out)

good_good_json = {}

for e in controller_xml.getiterator('Name'):
    name = e.text

for e in controller_xml.getiterator('FirmwareVer'):
    fw_ver = e.text

for e in controller_xml.getiterator('RequiredFirmwareVersion'):
    latest_fw_ver = e.text

for e in controller_xml.getiterator('RebuildRate'):
    rebuild_rate = e.text

for e in controller_xml.getiterator('AlarmState'):
    alarm = e.text


good_good_json['Category'] = "RAID Controller"
good_good_json['ControllerName'] = name
good_good_json['FirmwareVersion'] = fw_ver
good_good_json['LastestFirwareVersion'] = latest_fw_ver
# Rebuild rate is a percent. Not sure what it means
good_good_json['RebuildRate'] = rebuild_rate
good_good_json['AlarmStatus'] = alarm



# Post JSON to API that talks to Mongo here:


"""    

list_columns = []
list_data = []

for line in controller_out.splitlines():
    if line == '':
        pass
    elif line == 'Controller':
        pass
    elif line == ' Controller  PERC H700 Integrated(Embedded)':
        pass
    elif 'ID' in line.split(';'):  
        list_columns.append(line.replace(';', ', '))
    else:
        list_data.append(line.replace(';', ', '))

zipped_goodness = zip(list_columns, list_data)
print(zipped_goodness)

controller_in = StringIO(controller_out)

reader = csv.reader(controller_in, delimiter=';')

line_count = 0
for row in reader:
    if line_count == 0:
        print(f'Columns: {"; ".join(row)}')
    else:
        print(f'\t{row[1]}')
    #print('\t'.join(row))
"""