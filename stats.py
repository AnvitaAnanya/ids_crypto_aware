# stats.py

stats = {
    "total_packets": 0,
    "alerts_triggered": 0,
    "detections": {
        "Keyword": 0,
        "Credit Card": 0,
        "SSN": 0,
        "API Key": 0
    }
}

def update_stat(type_label):
    stats["alerts_triggered"] += 1
    if type_label in stats["detections"]:
        stats["detections"][type_label] += 1

def increment_packet_count():
    stats["total_packets"] += 1

def get_stats():
    return stats
