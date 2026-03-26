from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # We only care about packets that have an IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Determine the protocol
        protocol = "Other"
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"

        print(f"[*] {src_ip} -> {dst_ip} | Protocol: {protocol}")

        # If it is a TCP packet, try to show a tiny snippet of the raw data
        if packet.haslayer(TCP) and packet.getlayer(TCP).payload:
            payload = str(packet.getlayer(TCP).payload)
            print(f"    [Data]: {payload[:60]}...")

def main():
    print("--- 📡 Network Packet Sniffer ---")
    print("[*] Listening for traffic... (Press Ctrl+C to stop)")
    
    # Start sniffing! 
    # store=0 ensures it doesn't eat up your laptop's RAM
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()