import requests, json
from config import *
class PostMetrics:

    headers = {'Content-Type': 'application/json'}
    def post(json_report):
        if verify_ssl:

            r = requests.post(api_server, headers=headers, data=json.dumps(json_report))
        elif not verify_ssl:
            r = requests.post(api_server, headers=headers, data=json.dumps(json_report), verify=False)
        
        else:
            print("Please specify ssl_verify in config.py")
        


