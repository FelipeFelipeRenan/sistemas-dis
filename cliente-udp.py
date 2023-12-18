import socket

# Endereço e porta do servidor
HOST = '127.0.0.1'
PORT = 12346

# Cria um socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Envia uma mensagem vazia para o servidor
    client_socket.sendto(b'', (HOST, PORT))

    # Recebe a resposta do servidor
    data, server_address = client_socket.recvfrom(1024)

    # Exibe a resposta
    print(f'Data do servidor ({server_address}): {data.decode("utf-8")}')

    # Aguarda um tempo (opcional)
    input("Pressione Enter para obter a data novamente...")
