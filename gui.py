# gui.py

import tkinter as tk
from tkinter import ttk
import threading
from sniffer import sniff_packets

# === COLOURS AND STYLES ===
BG_COLOR = "#f0f4f8"
HEADER_COLOR = "#4a90e2"
ALERT_BG = "#ffe6e6"      # light coral
STATS_BG = "#e0f7fa"      # light teal
KEYWORDS_BG = "#fff9c4"   # light yellow
TEXT_COLOR = "#333333"
FONT_HEADER = ("Segoe UI", 20, "bold")
FONT_TITLE = ("Segoe UI", 14, "bold")
FONT_BODY = ("Segoe UI", 11)

# === ROOT WINDOW ===
root = tk.Tk()
root.title("Crypto-Aware Intrusion Detection System")
root.geometry("1100x650")
root.configure(bg=BG_COLOR)

# === HEADER ===
header = tk.Label(
    root, text="🔐 Crypto-Aware Intrusion Detection System",
    bg=BG_COLOR, fg=HEADER_COLOR, font=FONT_HEADER
)
header.pack(pady=20)

# === MAIN CONTENT AREA ===
content = tk.Frame(root, bg=BG_COLOR)
content.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# === ALERTS SECTION ===
alerts_frame = tk.LabelFrame(
    content, text="🔔 Real-Time Alerts", bg=ALERT_BG, fg=TEXT_COLOR,
    font=FONT_TITLE, padx=10, pady=10, relief=tk.GROOVE, bd=2
)
alerts_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

alerts_display = tk.Text(
    alerts_frame, height=20, bg=ALERT_BG, fg="#b71c1c",
    font=FONT_BODY, wrap=tk.WORD, bd=0, relief=tk.FLAT
)
alerts_display.pack(fill=tk.BOTH, expand=True)

# === STATS SECTION ===
stats_frame = tk.LabelFrame(
    content, text="📊 System Stats", bg=STATS_BG, fg=TEXT_COLOR,
    font=FONT_TITLE, padx=10, pady=10, relief=tk.GROOVE, bd=2
)
stats_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

total_var = tk.StringVar(value="Total Packets: 0")
alert_var = tk.StringVar(value="Alerts Triggered: 0")
encrypted_var = tk.StringVar(value="Encrypted Packets: 0")

tk.Label(stats_frame, textvariable=total_var, bg=STATS_BG, fg=TEXT_COLOR, font=FONT_BODY).pack(anchor="w", pady=5)
tk.Label(stats_frame, textvariable=alert_var, bg=STATS_BG, fg=TEXT_COLOR, font=FONT_BODY).pack(anchor="w", pady=5)
tk.Label(stats_frame, textvariable=encrypted_var, bg=STATS_BG, fg=TEXT_COLOR, font=FONT_BODY).pack(anchor="w", pady=5)

# === KEYWORDS SECTION ===
keywords_frame = tk.LabelFrame(
    content, text="🕵️ Suspicious Keyword Hits", bg=KEYWORDS_BG, fg=TEXT_COLOR,
    font=FONT_TITLE, padx=10, pady=10, relief=tk.GROOVE, bd=2
)
keywords_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

keywords_display = tk.Text(
    keywords_frame, height=6, bg=KEYWORDS_BG, fg=TEXT_COLOR,
    font=FONT_BODY, wrap=tk.WORD, bd=0, relief=tk.FLAT
)
keywords_display.pack(fill=tk.BOTH, expand=True)

# === GRID CONFIG ===
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=2)
content.rowconfigure(0, weight=3)
content.rowconfigure(1, weight=1)

# === DATA DISPLAY CALLBACK ===
def display_alert(alert_msg, stats):
    alerts_display.insert(tk.END, alert_msg + "\n")
    alerts_display.yview(tk.END)

    total_var.set(f"Total Packets: {stats['total_packets']}")
    alert_var.set(f"Alerts Triggered: {stats['alerts_triggered']}")
    encrypted_var.set(f"Encrypted Packets: {stats['encrypted_packets']}")

    keywords_display.delete(1.0, tk.END)
    for keyword, count in stats["suspicious_keywords"].items():
        keywords_display.insert(tk.END, f"{keyword}: {count}\n")

# === RUN IDS THREAD ===
def run_ids():
    sniff_packets(callback=display_alert)

threading.Thread(target=run_ids, daemon=True).start()

# === MAINLOOP ===
root.mainloop()
