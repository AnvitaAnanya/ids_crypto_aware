test_packet_data = [
    b"username=admin&password=123456",    # Plaintext credentials (should alert)
    b"This is just random harmless data", # Harmless data
    b"token=abc123encryptedvalue",        # Possibly encrypted (shouldn't alert)
    b"creditcard=4111111111111111",       # Credit card (should alert)
    b"password=letmein123",               # Password in plain text (should alert)
    b"sessionid=xyz789",                  # Session ID (can be ignored or flagged if rule added)
    b"admin=true&login=granted",          # Contains keywords (should alert)
    b"apikey=encryptedvalue",             # Possibly encrypted
    b"login failed for user admin",       # Suspicious (should alert)
    b"hello world, nothing suspicious",   # Harmless
    b"social_security_number=123-45-6789",
]

