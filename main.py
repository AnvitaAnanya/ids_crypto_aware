# main.py

from sniffer import sniff_packets

if __name__ == "__main__":
    print("[*] Starting IDS...")
    sniff_packets()
    print("[*] IDS finished processing packets.")
