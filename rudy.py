import requests
from scapy.all import *

attack_sites = ["127.0.0.1"]


def send_packets(src="0.0.0.0", data=""):
    reduced_data = list(data)
    for seg_data in reduced_data:
        print (seg_data)
        packet = IP(dst=attack_sites[0], src=src) / TCP() / seg_data 
        send(packet)
    

send_packets(src="127.0.0.1", data="01189998819991197253")

