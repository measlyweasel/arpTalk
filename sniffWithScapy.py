
# In[13]:

##An Example of using scapy for sniffing
from scapy.all import *
sniff(iface=interface, prn=lambda x: x.show(), filter='tcp',count=1)


# Out[13]:

#     ###[ Ethernet ]###
#       dst       = 58:6d:8f:08:78:c9
#       src       = ba:db:ee:f1:23:45
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 89
#          id        = 13954
#          flags     = DF
#          frag      = 0L
#          ttl       = 64
#          proto     = tcp
#          chksum    = 0x210d
#          src       = 192.168.1.132
#          dst       = 173.194.115.33
#          \options   \
#     ###[ TCP ]###
#             sport     = 49181
#             dport     = https
#             seq       = 960262771
#             ack       = 3217359725
#             dataofs   = 8L
#             reserved  = 0L
#             flags     = PA
#             window    = 318
#             chksum    = 0xe35b
#             urgptr    = 0
#             options   = [('NOP', None), ('NOP', None), ('Timestamp', (586143, 2052748325))]
#     ###[ Raw ]###
#                load      = "\x17\x03\x01\x00 x\x89\xd2\x07X#\x8e\xa0\xd4\x9b\x98-5M\xdb\xe2>\xdd\x8c\xa6[H\xf29\x0cn$\xe7\xa6\x8f'\xdb"
# 

#     <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>

# In[ ]:



