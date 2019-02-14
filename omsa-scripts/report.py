#!/usr/bin/env python36
"""
yum -y install python36 python36-setuptools python36-devel
easy_install-3.6 pip
pip3 install requests
"""
import subprocess, requests
import xml.etree.ElementTree as ET

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_chassis_arg = "chassis"

# Define counters
cpu_count = 0
dimm_count = 0

# Define lists to zip later
cpu_list = []
memory_list = []

chassis_out = subprocess.check_output([dell_tool, dell_chassis_arg, '-fmt', 'xml']).decode('utf-8')

chassis_xml = ET.fromstring(chassis_out)

for e in chassis_xml.getiterator('ChassModel'):
    chassis_model = e.text
for e in chassis_xml.getiterator('ChassManufacturer'):
    chassis_manfacturer = e.text

#for e in chassis_xml.iter():
#    print("Tag: {} || Text: {}".format(e.tag, e.text))

serial_number = chassis_xml.findall('serialnumber')


for e in chassis_xml.iter('processor'):
    for c in e.iter():
        if c.tag == "Manufacturer":
            cpu_count += 1
            make = c.text
        elif c.tag == "Version":
            version = c.text
        elif c.tag == "coreCount":
            cores = c.text
        elif c.tag == "curSpeed":
            speed = c.text
        elif c.tag == "maxSpeed":
            max_speed = c.text
        list_addition = (cpu_count, [make, version, cores, speed, max_speed])
        cpu_list.append(list_addition)
        
print(cpu_list)
#print(make, version, str(cores), str(speed), str(max_speed))

        nice = """
            Make: {}
            Version: {}
            Cores: {}
            Current Speed: {}
            Max Speed: {}
            """.format(make, version, str(cores), str(speed), str(max_speed))

"""
Object types:
210 = CPU
23 = Chassis (?)
"""
post_ = post_metrics.PostMetrics()
r = post_.post(json_report)
print(r)