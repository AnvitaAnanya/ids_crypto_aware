# sniffer.py

import time
from test_packets import test_packet_data
from analyzer import analyze_packet, stats

def sniff_packets(callback=None):
    for packet in test_packet_data:
        alert_msg = analyze_packet(packet)
        if callback and alert_msg:
            callback(alert_msg, stats)
        time.sleep(1)
