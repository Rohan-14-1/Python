import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("LoRa Transmitter started...")
count = 0
while True:
    message = f"Packet #{count} | Temp: 25.{count}°C"
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    print(f"[SENT] {message}")
    count += 1
    time.sleep(2)