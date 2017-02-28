import requests
import json
import os
import sdnconfig

### Stop Emulation Test.

fp = open("/tmp/temp.txt","r")
test_id = fp.read()

def vx_sdn_stop_emulation ():
	session_ip = sdnconfig.emulation_host_ip
        url = "http://"+session_ip+"/VxSDN/emulation/test/stop"
        post_header = {'Content-Type': 'application/json','accept': 'application/json'}
        payload = {
                    "username":"admin",
                    "password":"admin",
                    "id":test_id }
        r=requests.post(url,json.dumps(payload),headers=post_header)
        output = json.loads(r.content)
        print "\n Emulation %s " %output['message']

vx_sdn_stop_emulation ()

os.remove("/tmp/temp.txt")
