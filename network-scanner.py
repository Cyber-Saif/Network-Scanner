#a simple network scanner
import scapy.all as scapy
ip = input("type your ip and range: ")

def scan(ip):
    ip_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    packet = broadcast/ip_request
    responsed_list = scapy.srp(packet, timeout= 1, verbose = False)[0]

    print("------------------------------------------")
    print("   IP \t\t\t       MAC")
    print("------------------------------------------")

    for responeses in responsed_list:
        print(responeses[1].psrc + "\t\t" + responeses[1].hwsrc)

scan(ip)
