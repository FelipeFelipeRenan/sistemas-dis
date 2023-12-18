import socket

# Endereço e porta do servidor
HOST = '127.0.0.1'
PORT = 12346

# Cria um socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((HOST, PORT))

# Recebe a data e hora do servidor
data = client_socket.recv(1024).decode('utf-8')

# Exibe a data e hora recebidas
print(f'Data do servidor ({HOST}:{PORT}): {data}')

# Fecha o socket do cliente
client_socket.close()
