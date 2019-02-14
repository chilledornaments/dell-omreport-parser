import requests, json
from config import *
class PostMetrics():

    headers = {'Content-Type': 'application/json'}
    def post(self, json_report):
        if verify_ssl:

            r = requests.post(api_server, headers=self.headers, data=json.dumps(json_report))
            return r
        elif not verify_ssl:
            r = requests.post(api_server, headers=self.headers, data=json.dumps(json_report), verify=False)
            return r
        
        else:
            return "Please specify ssl_verify in config.py"
        


