# 🛡️ Crypto-Aware Intrusion Detection System (IDS)

An anomaly-based intrusion detection system built with Python that monitors network packet payloads, flags suspicious activity (like plaintext credentials or encrypted messages), and provides a modern, colorful GUI for real-time visualization of alerts and traffic statistics.

---

## 📌 Features

- ✅ **Anomaly Detection**  
  Identifies suspicious patterns such as:
  - Plaintext credentials (`username`, `password`)
  - Payment information (`creditcard`, `cvv`)
  - Access tokens, sessions, and secrets

- 🔐 **Crypto Awareness**  
  Detects base64-encoded or encrypted payloads, useful in catching obfuscated attacks or data exfiltration.

- 🖥️ **Modern GUI**  
  Clean, colorful interface with distinct sections for:
  - **Live Alerts**: Instant notification of suspicious activity
  - **Traffic Stats**: Breakdown of packet categories
  - **Graphs**: Pie chart representing packet types or alert types

- 🧪 **Packet Simulation Ready**  
  Easily test without real network sniffing by using predefined payloads via `test_packets.py`.

---

## 🧰 Tech Stack

| Component       | Tech      |
|----------------|-----------|
| Language        | Python 3.10+ |
| GUI             | Tkinter (ttk themed) |
| Packet Simulator| Custom Python list of byte strings |
| Visualization   | Matplotlib (for graphs) |

---

## 🏗️ System Architecture



```
+------------------+
| test_packets.py  |  <-- Simulated packets
+------------------+
        |
        v
+------------------+       +---------------------+
|   sniffer.py     |-----> |   analyzer.py       |
+------------------+       +---------------------+
                                 |
            +--------------------+
            v
+----------------------+     +-----------------------+
| crypto_checker.py    |<--> | alerts.py             |
+----------------------+     +-----------------------+
            |
            v
+----------------------------+
|         gui.py            |  <-- Live GUI with stats + alerts
+----------------------------+
```

---

## 🗂️ File Structure

```bash
ids_crypto_aware/
├── main.py               # Entry point
├── gui.py                # GUI with real-time stats and alert display
├── sniffer.py            # Simulates/sniffs packets
├── analyzer.py           # Analyzes payloads
├── crypto_checker.py     # Checks if payload is encrypted
├── alerts.py             # Formats alert messages
├── test_packets.py       # Simulated network traffic
└── README.md             # Project documentation
```

---


### 2️⃣ Requirements

- Python 3.10+
- No external dependencies other than `matplotlib` for graph rendering:

## 💡 Example Use Cases

- Educational tool for understanding IDS systems
- Demonstrating security awareness through crypto/payload inspection
- Prototype for a larger security monitoring dashboard

---

## 🧠 Future Enhancements

- [ ] Switch to real network sniffing using `scapy`
- [ ] Export logs to `.csv` or `.json`
- [ ] Email/SMS alerts for critical issues
- [ ] Add timestamps and IP address simulation

---


## 📜 License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 🤝 Contributing

Want to make this even better?

1. Fork the repo
2. Make your changes
3. Submit a Pull Request ✅

---
