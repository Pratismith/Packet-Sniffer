# Packet Sniffer GUI

## Description
Packet Sniffer GUI is a network traffic monitoring tool built using Python. It captures and displays real-time network packets in a user-friendly graphical interface. Users can start and stop packet sniffing, as well as save captured packets in a `.pcap` file for further analysis.

## Features
- **Real-time Packet Capture**: Captures live network packets.
- **Graphical Interface**: User-friendly GUI using `tkinter`.
- **Packet Display**: Shows packet summaries in a scrollable text area.
- **Save Packets**: Exports captured packets as a `.pcap` file.
- **Start/Stop Control**: Users can control packet sniffing with buttons.

## Tools & Technologies Used
- **Python**: Core programming language.
- **Tkinter**: For building the GUI.
- **Scapy**: For packet sniffing and network analysis.
- **Threading**: To ensure smooth GUI operation while capturing packets.

## Installation
1. Install required dependencies:
   ```sh
   pip install scapy
   ```
2. Run the script:
   ```sh
   python script.py
   ```
   *(Linux users may need to run with sudo: `sudo python script.py`)*

## Usage
1. Click **"Start Sniffing"** to begin capturing network packets.
2. Click **"Stop Sniffing"** to stop capturing packets.
3. Click **"Save Packets"** to save captured packets as a `.pcap` file.

## Future Enhancements
- Add filters to capture specific protocols (e.g., TCP, UDP, HTTP, etc.).
- Implement live packet analysis with packet details.
- Improve UI with additional controls and customization options.

