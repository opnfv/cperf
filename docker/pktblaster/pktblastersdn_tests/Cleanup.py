#!/usr/local/python

'''
@description:stop emulation test
@arguments:test_id read from the temp file
@return:none
'''

import requests
import json
import os
import sdnconfig

file_descriptor = open("/tmp/temp.txt", "r")
test_id = file_descriptor.read()

def vx_sdn_stop_emulation():
    '''
    @description:emulation test stopped for the particular test_id
    @return:none
    '''
    session_ip = sdnconfig.emulation_host_ip
    url = "http://"+session_ip+"/VxSDN/emulation/test/stop"
    post_header = {'Content-Type': 'application/json',\
        'accept': 'application/json'}
    payload = {
        "username":"admin",
        "password":"admin",
        "id":test_id}
    req_output = requests.post(url, json.dumps(payload), headers=post_header)
    output = json.loads(req_output.content)
    print "\n Emulation %s " % output['message']

vx_sdn_stop_emulation()

os.remove("/tmp/temp.txt")
