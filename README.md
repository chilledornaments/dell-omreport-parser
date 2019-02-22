# dell-omreport-parser

## What is it?

This tool uses the Dell `omreport` tool to output an XML, format it to a JSON, and send it to an API server to gather inventory and trigger alerts.

Check the API section for info on the API/Web server.

## Compatability 

This has been tested with and written for OMSA Version 8.3.0

The temperature and power supply scripts have issues collecting data for OMSA Version 9.2.0. Workaround in the `WORKAROUNDS` section

To find the version of OMSA running on your server (for Linux hosts at least), run `/opt/dell/srvadmin/sbin/omreport about`
## How To

- Clone repo in `/opt/`

- Move `omsa-scripts/config.example.py` to `omsa-scripts/config.py`

- Edit `omsa-scripts/config.py`
    - `host` is the name of the server
    - `api_server` is the OMSA-Web server. See the API section for more info.
    - `verify_ssl` determines whether or not `requests` will verify the TLS certificate when posting metrics

- Run `install.sh` as root

If you want to clone the repo elsewhere, you'll need to modify `/etc/cron.d/omsa-metrics`.

## API

Metrics are sent to an API server that you define. 

The API server can be found in [this repo](https://github.com/mitchya1/dell-omreport-web)

## WORKAROUNDS

### 9.2.0 Temperature

```
#!/usr/bin/env python36
# ./omreport chassis temps -fmt xml
import xml.etree.ElementTree as ET
import subprocess, requests, json, post_metrics
from config import *

dell_tool = "/opt/dell/srvadmin/sbin/omreport"
dell_arg = "chassis"
dell_arg_two = "temps"

host = host
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
                if name != "Mainboard MB Temp":
                    pass
                else:
                    
                    json_ = {"TempReading": name, "TempInC": temp}
                    #print(json_)
                    json_report['Report'][name] = json_


post_ = post_metrics.PostMetrics()
r = post_.post(json_report)
print(r)
```
