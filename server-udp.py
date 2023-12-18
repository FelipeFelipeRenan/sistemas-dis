import socket
import threading
from datetime import datetime

def conexao_cliente(client, address):
    try:
        print(f'Conexão recebida de {address}')

        # Obtém a data e hora atuais
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Envia a data e hora para o cliente
        client.sendall(current_time.encode('utf-8'))
    finally:
        # Fecha o socket do cliente
        client.close()

# Endereço e porta do servidor
HOST = '127.0.0.1'
PORT = 12345

# Cria um socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket ao endereço e porta
sock.bind((HOST, PORT))

# Escuta por conexões entrantes
sock.listen()

print(f'Servidor TCP aguardando conexões em {HOST}:{PORT}')

while True:
    # Aceita uma conexão
    client, address = sock.accept()

    # Cria uma nova thread para lidar com o cliente
    conexao = threading.Thread(target=conexao_cliente, args=(client, address))
    conexao.start()
