import socket

# Configurações
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 5000))
next_router = ('router4', 5000)  # Próximo roteador é o Router 4

try:
    while True:
        data, address = sock.recvfrom(4096)
        sock.sendto(data, next_router)

finally:
    sock.close()
