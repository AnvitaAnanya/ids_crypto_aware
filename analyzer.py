# analyzer.py

from crypto_checker import is_encrypted
from alerts import log_alert

SUSPICIOUS_KEYWORDS = [
    b'username', b'password', b'login', b'admin', b'auth',
    b'creditcard', b'social_security_number', b'api_key'
]

stats = {
    'total_packets': 0,
    'alerts_triggered': 0,
    'encrypted_packets': 0,
    'suspicious_keywords': {}
}

def analyze_packet(raw_data):
    stats['total_packets'] += 1
    alert_triggered = False

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in raw_data.lower():
            if not is_encrypted(raw_data):
                alert_triggered = True
                stats['alerts_triggered'] += 1
                key_str = keyword.decode()
                stats['suspicious_keywords'][key_str] = stats['suspicious_keywords'].get(key_str, 0) + 1
                alert_msg = f"[!] Suspicious packet detected: keyword '{key_str}' in plain text!"
                print(alert_msg)
                log_alert(alert_msg)
                return alert_msg  # Return for GUI callback
            else:
                stats['encrypted_packets'] += 1

    return None  # No alert
