from socket import *
server_port = 6789
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("127.0.0.1", server_port))
print("The server is ready to receive msg...")
while True:

    key, client_address = server_socket.recvfrom(2048)
    result = ""
    key = int(key.decode('utf-8'))
    text = 'ATTACKATONCE'
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    modified_message = result.upper()
    server_socket.sendto(modified_message.encode('utf-8'), client_address)

