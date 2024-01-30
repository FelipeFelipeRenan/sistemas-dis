from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2', )

# Lista para armazenar mensagens no servidor
mensagem_lista = []

def armazenar_mensagem(mensagem):
    mensagem_lista.append(mensagem)
    return "Mensagem armazenada com sucesso!"

def recuperar_mensagens():
    return mensagem_lista

def obter_ip_servidor():
    return "IP do servidor: localhost"

def obter_data_hora_servidor():
    agora = datetime.now()
    return agora.strftime("%Y-%m-%d %H:%M")

with SimpleXMLRPCServer(('localhost', 21212), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(armazenar_mensagem, 'armazenar_mensagem')
    server.register_function(recuperar_mensagens, 'recuperar_mensagens')
    server.register_function(obter_ip_servidor, 'obter_ip_servidor')
    server.register_function(obter_data_hora_servidor, 'obter_data_hora_servidor')

    server.serve_forever()
