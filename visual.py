from scapy.all import sniff

# Callback function to handle packets
def packet_callback(packet):
    # Print a summary of each packet received
    print(packet.summary())  # Prints basic info (e.g., source, destination, protocol)

# Start sniffing packets
def start_sniffing():
    print("[*] Starting packet sniffing...")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffing()
