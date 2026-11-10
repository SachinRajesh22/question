import socket
import struct

server = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("RAW SOCKET PACKET CAPTURE")
print("Press Ctrl+C to stop...\n")

while True:

    data, addr = server.recvfrom(65536)

    # Ethernet Header
    dest_mac = ':'.join('%02x' % b for b in data[0:6])
    src_mac = ':'.join('%02x' % b for b in data[6:12])

    protocol = struct.unpack('!H', data[12:14])[0]

    print("\n-----------------------------")
    print("Destination MAC :", dest_mac)
    print("Source MAC      :", src_mac)
    print("Ethernet Protocol:", hex(protocol))

    # IPv4 Packet
    if protocol == 8:

        ip_header = data[14:34]

        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

        ttl = iph[5]
        proto = iph[6]

        src_ip = socket.inet_ntoa(iph[8])
        dest_ip = socket.inet_ntoa(iph[9])

        print("\nIP Header")
        print("Source IP      :", src_ip)
        print("Destination IP :", dest_ip)
        print("TTL            :", ttl)
        print("Protocol       :", proto)

        # TCP
        if proto == 6:

            tcp_header = data[14 + (iph[0] & 15) * 4:]

            tcp = struct.unpack('!HH', tcp_header[:4])

            print("\nTCP Header")
            print("Source Port      :", tcp[0])
            print("Destination Port :", tcp[1])

        # UDP
        elif proto == 17:

            udp_header = data[14 + (iph[0] & 15) * 4:]

            udp = struct.unpack('!HH', udp_header[:4])

            print("\nUDP Header")
            print("Source Port      :", udp[0])
            print("Destination Port :", udp[1])

        # ICMP
        elif proto == 1:

            icmp_header = data[14 + (iph[0] & 15) * 4:]

            icmp = struct.unpack('!BB', icmp_header[:2])

            print("\nICMP Header")
            print("Type :", icmp[0])
            print("Code :", icmp[1])

        else:
            print("Other Protocol")