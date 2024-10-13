import socket
import time

# Configurações
server_address = ('router1', 5000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start_time = time.time()
end_time = start_time + 1 * 60  # 5 minutos
count = 0

# Definir um timeout de 10 segundos para evitar travamentos
sock.settimeout(10)

try:
    # Envio de mensagens por 5 minutos
    while time.time() < end_time:
        message = f'Message {count}'
        sock.sendto(message.encode(), server_address)
        count += 1
        time.sleep(0.01)
        print(f"Sent: {message}")

    # Envio da mensagem final
    sock.sendto("The End".encode(), server_address)
    print("Sent: The End")

    # Tentar receber do receiver o número de mensagens recebidas
    try:
        data, receiver_address = sock.recvfrom(4096)
        received_count = int(data.decode())
        print(f"Messages received: {received_count}")
    except socket.timeout:
        print("Timeout: No response from receiver")

    # Cálculo da taxa de mensagens perdidas
    lost_messages = count - received_count if 'received_count' in locals() else count
    loss_rate = (lost_messages / count) * 100 if count > 0 else 0
    print(f"Messages sent: {count}")
    print(f"Messages lost: {lost_messages}")
    print(f"Loss rate: {loss_rate:.2f}%")

finally:
    sock.close()
    print(f"Sender finished after sending {count} messages")
