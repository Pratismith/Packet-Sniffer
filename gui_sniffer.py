import tkinter as tk
from tkinter import scrolledtext, filedialog
import threading
from scapy.all import sniff, wrpcap

class PacketSnifferGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Packet Sniffer GUI")
        self.root.geometry("700x500")

        # Title
        tk.Label(root, text="Packet Sniffer", font=("Arial", 16, "bold")).pack(pady=5)

        # Packet Display Box
        self.text_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.text_area.pack(padx=10, pady=5)

        # Buttons Frame
        frame = tk.Frame(root)
        frame.pack(pady=5)

        # Start Button
        self.start_btn = tk.Button(frame, text="Start Sniffing", command=self.start_sniffing, bg="green", fg="white")
        self.start_btn.grid(row=0, column=0, padx=5)

        # Stop Button
        self.stop_btn = tk.Button(frame, text="Stop Sniffing", command=self.stop_sniffing, state=tk.DISABLED, bg="red", fg="white")
        self.stop_btn.grid(row=0, column=1, padx=5)

        # Save Button
        self.save_btn = tk.Button(frame, text="Save Packets", command=self.save_packets, state=tk.DISABLED, bg="blue", fg="white")
        self.save_btn.grid(row=0, column=2, padx=5)

        # Sniffing Flag
        self.sniffing = False
        self.packets = []

    def start_sniffing(self):
        """Start packet sniffing in a separate thread."""
        self.sniffing = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.save_btn.config(state=tk.DISABLED)

        self.sniff_thread = threading.Thread(target=self.sniff_packets, daemon=True)
        self.sniff_thread.start()

    def stop_sniffing(self):
        """Stop packet sniffing."""
        self.sniffing = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.save_btn.config(state=tk.NORMAL)

    def sniff_packets(self):
        """Capture packets and display in GUI."""
        self.packets = sniff(prn=self.display_packet, store=True, stop_filter=lambda x: not self.sniffing)

    def display_packet(self, packet):
        """Display packet in the text area."""
        self.text_area.insert(tk.END, f"{packet.summary()}\n")
        self.text_area.see(tk.END)

    def save_packets(self):
        """Save captured packets to a .pcap file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".pcap", filetypes=[("PCAP files", "*.pcap")])
        if file_path:
            wrpcap(file_path, self.packets)
            self.text_area.insert(tk.END, f"\nSaved packets to: {file_path}\n")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PacketSnifferGUI(root)
    root.mainloop()
