import socket
import random

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("LoRa Receiver listening...")
while True:
    data, addr = sock.recvfrom(1024)
    rssi = random.randint(-120, -40)  # Simulated signal strength
    snr = round(random.uniform(-5, 10), 1)  # Simulated SNR
    print(f"[RECEIVED] {data.decode()} | RSSI: {rssi} dBm | SNR: {snr} dB")