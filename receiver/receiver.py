import socket
import time
import statistics

# Configurações
server_address = ('', 5000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

messages_received = []
start_time = time.time()

try:
    while True:
        data, address = sock.recvfrom(4096)
        current_time = time.time()
        message = data.decode()

        # Verificar se a mensagem recebida é "The End"
        if message == "The End":
            print("Received: The End")
            break
        messages_received.append(current_time)

    # Enviar de volta o número de mensagens recebidas
    response_message = f'{len(messages_received)}'
    print(f"Messages received: {len(messages_received)}")
    sock.sendto(response_message.encode(), address)

finally:
    # Calcular as estatísticas de taxa de recebimento
    if len(messages_received) > 1:
        intervals = [t2 - t1 for t1, t2 in zip(messages_received, messages_received[1:])]
        avg_rate = 1 / statistics.mean(intervals) if intervals else 0
        max_rate = 1 / min(intervals) if intervals else 0
        min_rate = 1 / max(intervals) if intervals else 0
        std_dev = statistics.stdev(intervals) if len(intervals) > 1 else 0

        print(f'Avg rate: {avg_rate:.3f} msgs/s')
        print(f'Max rate: {max_rate:.3f} msgs/s')
        print(f'Min rate: {min_rate:.3f} msgs/s')
        print(f'Std dev: {std_dev:.3f}')

    sock.close()
