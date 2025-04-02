from scapy.all import sniff
import datetime

# Function to log packet details
def packet_callback(packet):
    log_entry = f"{datetime.datetime.now()} | {packet.summary()}\n"
    print(log_entry.strip())  # Print packet details

    with open("packet_log.txt", "a") as log_file:
        log_file.write(log_entry)

# Start sniffing
print("Sniffing started... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)
