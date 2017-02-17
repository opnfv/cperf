#!/usr/bin/python

from xml.etree.ElementTree import ElementTree, SubElement, tostring, XML
import xml.etree.ElementTree as etree
import xml.etree.cElementTree as ET
from xml.dom import minidom
import sys
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
import io
import sys,os
import datetime
from sdnconfig import *
import requests, json, shutil
import getopt

switches =""
controller_node_ip =""

### Configuartion from argument list
def cmdarg(argv):
        try:
                opts, args = getopt.getopt(argv,"s:i:h",["switch_count=","controller_node_ip="])
        except getopt.GetoptError:
		print 'python sdn_topology.py --switch_count <switch count> --controller_node_ip <odl controller node ip>'
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
			print 'python sdn_topology.py --switch_count <switch count> --controller_node_ip <odl controller node ip>'
                        sys.exit()
                elif opt in ("-s", "--switch_count"):
                        global switches
			switches = arg
                elif opt in ("-i", "--controller_node_ip"):
                        global controller_node_ip
			controller_node_ip = arg

if __name__ == "__main__":
   cmdarg(sys.argv[1:])

name = filename
filename=name+'.xml'
sw= int(switches)
outFile = open(filename, 'w')
generated_on = str(datetime.datetime.now())
tmp = open("/tmp/temp.txt", 'w')
page = etree.Element("topology")

doc = etree.Element(page)


#switches=int(raw_input('Enter no of switches: '))

### Printing the switch connections ###
x=78
y=67
for i in range(1,sw+1):
        t="S"
	t=t+str(i)
	if i%9 == 0:
		x = 78
		y=y+35
	bodyElt = etree.SubElement(page, "d i='%s' g='S' t='%s' c='4' x='%s' y='%s' s=';Black' e='true' p=''" %(i,t,x,y))
	if i == sw:
		lsx=x
		lsy=y
	x=x+108


### Printing the Traffic End points connections ###

for i in range(1,3):
	x=78
        y=67
        t="TEP"
	t=t+str(i)
	if t == "TEP1":
	    x=x-(x-1)
	    y=y-7
	else:
	    x=lsx+x
            y=lsy-7

	body = etree.SubElement(page, "d i='%s' g='TEP' t='%s' c='1' x='%s' y='%s' s=';Black' e='true' p=''" %(i,t,x,y))


### Printing the switch port connection ###

for i in range(1,sw):
	s="S"
	j=i+1
	p1=s+str(i)+"_"+"2"
	p2=s+str(j)+"_"+"1"

	if j==s:
            break
	ports = etree.SubElement(page, "l p1='%s' p2='%s' v=''" %(p1,p2))

for i in range(1,3):
	t="TEP"
	j=1
	t=t+str(i)+"_"+str(j)
	s="S"
	if i == 1:
	    temp1 = t
            first_sw =s+str(i)+"_"+str(i)
            TEP = etree.SubElement(page, "l p1='%s' p2='%s' v='' " %(temp1,first_sw)) 
	else:
	    temp2=t
            last_sw = s+str(switches)+"_"+str(i)
	    TEP = etree.SubElement(page, "l p1='%s' p2='%s' v='' " %(last_sw,temp2))

tree = ET.ElementTree(page)
tree.write(filename, encoding='ISO-8859-1', xml_declaration=True)



outFile.close()
source = os.getcwd() +"/"+str (filename)
#print source
destination = r"/usr/local/tomcat-6.0.18/webapps/VxSDN/Resources/topologies/Custom Topology/"+filename
#print destination
shutil.move( source, destination)


#################################################################################
#FUNCTION TO SET CONTROLLER
#################################################################################

def vx_sdn_set_controller ():	
	session_ip = emulation_host_ip
	username = "admin"
	password = "admin"
	controller_ip = controller_node_ip
	controller_name = controllername
	build_version = buildversion
	openflow_mode = openflowmode
	openflow_port = controllerport
	openflow_version = openflowversion

	url= "http://"+session_ip+"/VxSDN/performance/controller/set"
	post_header={'Content-Type': 'application/json','accept': 'application/json'}
	payload=  {
	"username": username,
	"password":password,
	"action":"add",
	"controllers":[{
                	"ip":controller_ip,
                	"name":controller_name,
                	"port":openflow_port,
                	"connection_mode":openflow_mode,
                	"build_version":build_version,
                	"controller_of_version":[openflow_version]
               		}]
	}
	r=requests.post(url,json.dumps(payload),headers=post_header)
	result = json.loads(r.content)
	message = result.get("message", {})
	if message:
		controller_id = message.split(':')[1]
		controller_id = controller_id.strip()
		return controller_id

	if result["result"].upper() != "OK":
		print result["error"]
		return 0
	return 1

controller_id = vx_sdn_set_controller ()

####################################
# FUNCTION TO START EMULATION TEST #
####################################
def vx_sdn_start_emulation ():

	session_ip = emulation_host_ip   #raw_input ("Enter Session IP: ")
	topology_name = str(name)
	controller_ip =  controller_node_ip #raw_input ("Enter controller_ip: ")
	controller_name = "ODL"
	controller_port = "6653"
	stp_mode = "yes"
	controller_versions = "1.3"

	url = "http://"+session_ip+"/VxSDN/emulation/test/start"
	post_header = {'Content-Type': 'application/json','accept': 'application/json'}
	payload = {
                       "topology_name": topology_name,
                       "controller_id":controller_id,
                       "controller_name":controller_name,
                       "controller_port":controller_port,
                       "stp_mode":stp_mode,
                       "controller_of_verions":[controller_versions],
                       "username":"admin",
                       "password":"admin"}
	r=requests.post(url,json.dumps(payload),headers=post_header)
	output = json.loads(r.content)
	message = output.get("message", {})
	tmp.write(message)
	print "\n Emulation Test Started with ID :  %s " %output['message']

vx_sdn_start_emulation ()
tmp.close()
