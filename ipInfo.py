from scapy.all import *
import socket
import netifaces

interface = 'eth0'
victimIp = '192.168.1.101'

def isMyRoute(x):
	return x[3] == interface and x[2] != '0.0.0.0'

ips = { 
	'interface': interface,
	'routerIp': [x[2] for x in scapy.all.conf.route.routes if isMyRoute(x)][0],
	'myIp': netifaces.ifaddresses(interface)[socket.AF_INET][0]["addr"],
	'victimIp': victimIp
}

routerIp = ips['routerIp']
myIp=ips['myIp']

def printIpInfo():	
	for key,value in ips.iteritems():
		print '{0:10}: {1:20}'.format(key, value)
