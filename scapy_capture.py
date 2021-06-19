from scapy.all import *

def capture_packet():
    packets = open("Paquetes Redes/packets.bin", "wb")
    scan = sniff(count = 1)
    for i in range(len(scan)):
        #hexdump(scan[i])
        packet = raw(scan[i])
        packets.write(packet)
        packets.seek(0)
    packets.close()