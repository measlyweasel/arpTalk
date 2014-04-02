
# In[ ]:

##An Example of using scapy for sniffing
from scapy.all import *


# In[ ]:

interface = 'eth0'
victimIp = '172.17.145.200'


# In[ ]:

def forwardOrModify(packet):
    packet.show()
    if (IP in packet and packet['IP'].src == victimIp):
        ## this is going to take care of http request, dns etc.
        print('found one to forward to the router')
    elif (packet['IP'].dst == victimIp):
        if (TCP in packet and packet['TCP'].sport == 'http'):
            print 'found one to modify'
        else:
            print 'found one to forward to the victim without modifying'
        


# In[6]:

sniff(iface=interface, prn=forwardOrModify, filter='ip and host ' + victimIp, count=50)


# Out[6]:

#     ###[ Ethernet ]###
#       dst       = 08:00:27:c9:5b:fe
#       src       = 08:00:27:af:c0:01
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 52
#          id        = 515
#          flags     = DF
#          frag      = 0L
#          ttl       = 128
#          proto     = tcp
#          chksum    = 0xdefd
#          src       = 172.17.145.200
#          dst       = 173.194.46.39
#          \options   \
#     ###[ TCP ]###
#             sport     = 49179
#             dport     = http
#             seq       = 660010407
#             ack       = 0
#             dataofs   = 8L
#             reserved  = 0L
#             flags     = S
#             window    = 8192
#             chksum    = 0x57e9
#             urgptr    = 0
#             options   = [('MSS', 1460), ('NOP', None), ('WScale', 2), ('NOP', None), ('NOP', None), ('SAckOK', '')]
#     found one to forward to the router
#     ###[ Ethernet ]###
#       dst       = 08:00:27:c9:5b:fe
#       src       = 08:00:27:af:c0:01
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 52
#          id        = 516
#          flags     = DF
#          frag      = 0L
#          ttl       = 128
#          proto     = tcp
#          chksum    = 0xdefc
#          src       = 172.17.145.200
#          dst       = 173.194.46.39
#          \options   \
#     ###[ TCP ]###
#             sport     = 49179
#             dport     = http
#             seq       = 660010407
#             ack       = 0
#             dataofs   = 8L
#             reserved  = 0L
#             flags     = S
#             window    = 8192
#             chksum    = 0x57e9
#             urgptr    = 0
#             options   = [('MSS', 1460), ('NOP', None), ('WScale', 2), ('NOP', None), ('NOP', None), ('SAckOK', '')]
#     found one to forward to the router
#     ###[ Ethernet ]###
#       dst       = 08:00:27:c9:5b:fe
#       src       = 08:00:27:af:c0:01
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 48
#          id        = 517
#          flags     = DF
#          frag      = 0L
#          ttl       = 128
#          proto     = tcp
#          chksum    = 0xdeff
#          src       = 172.17.145.200
#          dst       = 173.194.46.39
#          \options   \
#     ###[ TCP ]###
#             sport     = 49179
#             dport     = http
#             seq       = 660010407
#             ack       = 0
#             dataofs   = 7L
#             reserved  = 0L
#             flags     = S
#             window    = 8192
#             chksum    = 0x6bf2
#             urgptr    = 0
#             options   = [('MSS', 1460), ('NOP', None), ('NOP', None), ('SAckOK', '')]
#     found one to forward to the router
#     ###[ Ethernet ]###
#       dst       = 08:00:27:c9:5b:fe
#       src       = 08:00:27:af:c0:01
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 52
#          id        = 518
#          flags     = DF
#          frag      = 0L
#          ttl       = 128
#          proto     = tcp
#          chksum    = 0x7daa
#          src       = 172.17.145.200
#          dst       = 172.17.145.40
#          \options   \
#     ###[ TCP ]###
#             sport     = 49180
#             dport     = http
#             seq       = 2458192289
#             ack       = 0
#             dataofs   = 8L
#             reserved  = 0L
#             flags     = S
#             window    = 8192
#             chksum    = 0x776f
#             urgptr    = 0
#             options   = [('MSS', 1460), ('NOP', None), ('WScale', 2), ('NOP', None), ('NOP', None), ('SAckOK', '')]
#     found one to forward to the router
#     ###[ Ethernet ]###
#       dst       = 08:00:27:af:c0:01
#       src       = 08:00:27:c9:5b:fe
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 52
#          id        = 0
#          flags     = DF
#          frag      = 0L
#          ttl       = 64
#          proto     = tcp
#          chksum    = 0xbfb0
#          src       = 172.17.145.40
#          dst       = 172.17.145.200
#          \options   \
#     ###[ TCP ]###
#             sport     = http
#             dport     = 49180
#             seq       = 2329973101
#             ack       = 2458192290
#             dataofs   = 8L
#             reserved  = 0L
#             flags     = SA
#             window    = 29200
#             chksum    = 0x7b3a
#             urgptr    = 0
#             options   = [('MSS', 1460), ('NOP', None), ('NOP', None), ('SAckOK', ''), ('NOP', None), ('WScale', 7)]
#     found one to forward to the victim without modifying
#     ###[ Ethernet ]###
#       dst       = 08:00:27:c9:5b:fe
#       src       = 08:00:27:af:c0:01
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 40
#          id        = 519
#          flags     = DF
#          frag      = 0L
#          ttl       = 128
#          proto     = tcp
#          chksum    = 0x7db5
#          src       = 172.17.145.200
#          dst       = 172.17.145.40
#          \options   \
#     ###[ TCP ]###
#             sport     = 49180
#             dport     = http
#             seq       = 2458192290
#             ack       = 2329973102
#             dataofs   = 5L
#             reserved  = 0L
#             flags     = A
#             window    = 16425
#             chksum    = 0x7bb4
#             urgptr    = 0
#             options   = {}
#     ###[ Padding ]###
#                load      = '\x00\x00\x00\x00\x00\x00'
#     found one to forward to the router
#     ###[ Ethernet ]###
#       dst       = 08:00:27:c9:5b:fe
#       src       = 08:00:27:af:c0:01
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 448
#          id        = 520
#          flags     = DF
#          frag      = 0L
#          ttl       = 128
#          proto     = tcp
#          chksum    = 0x7c1c
#          src       = 172.17.145.200
#          dst       = 172.17.145.40
#          \options   \
#     ###[ TCP ]###
#             sport     = 49180
#             dport     = http
#             seq       = 2458192290
#             ack       = 2329973102
#             dataofs   = 5L
#             reserved  = 0L
#             flags     = PA
#             window    = 16425
#             chksum    = 0x65c
#             urgptr    = 0
#             options   = []
#     ###[ Raw ]###
#                load      = 'GET / HTTP/1.1\r\nAccept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*\r\nAccept-Language: en-US\r\nUser-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)\r\nAccept-Encoding: gzip, deflate\r\nHost: 172.17.145.40\r\nConnection: Keep-Alive\r\n\r\n'
#     found one to forward to the router
#     ###[ Ethernet ]###
#       dst       = 08:00:27:af:c0:01
#       src       = 08:00:27:c9:5b:fe
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 40
#          id        = 48099
#          flags     = DF
#          frag      = 0L
#          ttl       = 64
#          proto     = tcp
#          chksum    = 0x3d9
#          src       = 172.17.145.40
#          dst       = 172.17.145.200
#          \options   \
#     ###[ TCP ]###
#             sport     = http
#             dport     = 49180
#             seq       = 2329973102
#             ack       = 2458192698
#             dataofs   = 5L
#             reserved  = 0L
#             flags     = A
#             window    = 237
#             chksum    = 0x7b2e
#             urgptr    = 0
#             options   = {}
#     found one to forward to the victim without modifying
#     ###[ Ethernet ]###
#       dst       = 08:00:27:c9:5b:fe
#       src       = 08:00:27:af:c0:01
#       type      = 0x800
#     ###[ IP ]###
#          version   = 4L
#          ihl       = 5L
#          tos       = 0x0
#          len       = 40
#          id        = 521
#          flags     = DF
#          frag      = 0L
#          ttl       = 128
#          proto     = tcp
#          chksum    = 0x7db3
#          src       = 172.17.145.200
#          dst       = 172.17.145.40
#          \options   \
#     ###[ TCP ]###
#             sport     = 49180
#             dport     = http
#             seq       = 2458192698
#             ack       = 2329973102
#             dataofs   = 5L
#             reserved  = 0L
#             flags     = RA
#             window    = 0
#             chksum    = 0xba41
#             urgptr    = 0
#             options   = {}
#     ###[ Padding ]###
#                load      = '\x00\x00\x00\x00\x00\x00'
#     found one to forward to the router
# 

#     <Sniffed: TCP:9 UDP:0 ICMP:0 Other:0>

# In[ ]:



