import requests, socket
from scapy.all import *
from time import sleep
import os

attack_sites = ["127.0.0.1"]

def connect_to_site(dest_ip="0.0.0.0", port=443):
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_connection.connect((dest_ip,port))
    return socket_connection


def craft_packet(src_ip="0.0.0.0", data=""):
    reduced_data = list(data)
    for seg_data in reduced_data:
        print("in for loop")
        print (seg_data)
        packet = IP(dst=attack_sites[0], src=src_ip) / TCP() / seg_data 
        sleep(1)
    return packet
    
def send_packet(src_ip="0.0.0.0", data="", dest_ip="0.0.0.0", port=443):
    socket_connection = connect_to_site(dest_ip, port)
    packet = craft_packet(src_ip, data=data)
    socket_connection.send(bytes(packet))

send_packet(src_ip="127.0.0.1", data="test", dest_ip=attack_sites[0], port=80)
