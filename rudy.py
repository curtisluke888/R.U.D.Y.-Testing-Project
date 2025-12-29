import requests, socket
from scapy.all import *
from time import sleep
import random
import string
import os
import random

attack_sites = ["127.0.0.1"]

def connect_to_site(dest_ip="0.0.0.0", port=443):
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_connection.connect((dest_ip,port))
    return socket_connection


def craft_packet(src_ip="0.0.0.0", data=""):

    print (seg_data)
    packet = IP(dst=attack_sites[0], src=src_ip) / TCP() / seg_data

    return packet

def send_packets(src_ip="0.0.0.0", data="", dest_ip="0.0.0.0", port=443):
    socket_connection = connect_to_site(dest_ip, port)

    reduced_data = list(data)
    
    for d in reduced_data: 
        packet = craft_packet(src_ip, data=data)
        socket_connection.send(bytes(packet))
        sleep(1)

def generate_bogus_data(length_of_data=1000):
    data = ""

    for _ in range(length_of_data):
        data += (random.choice(string.ascii_lowercase))

    return data

#send_packets(src_ip="127.0.0.1", data=generate_bogus_data(), dest_ip=attack_sites[0], port=80)
