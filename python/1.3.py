from scapy.all import *
import time


for i in range(1,300):
        a= IP()
        a.dst = '23.210.254.113'# ip of ynet.co.il
        print("ttl = ",i)
        a.ttl = i
        b = ICMP()
        send(a/b)
        time.sleep(1)
