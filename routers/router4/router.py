import socket

# Configurações
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 5000))
receiver = ('receiver', 5000)  # Enviar diretamente para o Receiver

try:
    while True:
        data, address = sock.recvfrom(4096)
        sock.sendto(data, receiver)

finally:
    sock.close()
