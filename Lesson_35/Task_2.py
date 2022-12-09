import socket
import random

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

Key = str(random.randint(1, 30)).encode('utf-8')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.sendto(Key, (UDP_IP_ADDRESS, UDP_PORT_NO))
message, client_address = server_socket.recvfrom(2048)
print(str(message))
