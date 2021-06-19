from scapy_capture import capture_packet as capture
from ethernet import Ethernet
from ipv4 import IPv4
from icmpv4 import ICMPv4
from arp import ARP
from ipv6 import IPv6
from icmpv6 import ICMPv6
from tcp import TCP
from udp import UDP
from dns import DNS

file = 'packets.bin'
output = ""
ok = 's'

while ok.lower() == 's':
    if __name__ == "__main__":
        capture()
        # ? Ethernet
        ethernet = Ethernet(file) 
        output = str(ethernet)

        # * IPv4 -> ICMPv4
        if ethernet.getProtocol() == 'IPv4':
            ipv4 = IPv4(file)
            output += str(ipv4)

            if ipv4.getNextHeader() == 'ICMPv4': 
                icmpv4 = ICMPv4(file)  
                output += str(icmpv4)

            elif ipv4.getNextHeader() == 'TCP':
                tcp = TCP(file, byte=34)
                output += str(tcp)

                if tcp.destination_service == 53 or tcp.source_service == 53:
                    dns = DNS(file, byte=54)
                    output += str(dns)

            elif ipv4.getNextHeader() == 'UDP':
                udp = UDP(file, byte=34)
                output += str(udp)

                if udp.destination_service == 53 or udp.source_service == 53:
                    dns = DNS(file, byte=42)
                    output += str(dns)

        # ! ARP/RARP
        elif ethernet.getProtocol() == 'ARP' or ethernet.getProtocol() == 'RARP':
            arp = ARP(file) 
            output += str(arp)

        # TODO IPv6:
        else:
            ipv6 = IPv6(file)
            output += str(ipv6)

            if ipv6.getNextHeader() == 'ICMPv6':
                icmpv6 = ICMPv6(file)
                output += str(icmpv6)

            elif ipv6.getNextHeader() == 'TCP':
                tcp = TCP(file, byte=54)
                output += str(tcp)

                if tcp.destination_service == 53 or tcp.source_service == 53:
                    dns = DNS(file, byte=74)
                    output += str(dns)

            elif ipv6.getNextHeader() == 'UDP':
                udp = UDP(file, byte=54)
                output += str(udp)

                if udp.destination_service == 53 or udp.source_service == 53:
                    dns = DNS(file, byte=62)
                    output += str(dns)
        
        print(output)
        ok = input('\nContinuar? (s/n): ')