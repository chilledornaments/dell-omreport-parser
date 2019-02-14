import requests, json
from config import *
class PostMetrics:

    headers = {'Content-Type': 'application/json'}
    def post(json_report):
        if verify_ssl:

            r = requests.post(api_server, headers=headers, data=json.dumps(json_report))
            return r.status_code
        elif not verify_ssl:
            r = requests.post(api_server, headers=headers, data=json.dumps(json_report), verify=False)
            return r.status_code
        
        else:
            return "Please specify ssl_verify in config.py"
        


