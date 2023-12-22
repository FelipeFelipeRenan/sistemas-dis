import socketserver
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class RPCFunctions:
    def __init__(self):
        self.call_count = 0

    def get_current_datetime(self):
        self.call_count += 1
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_call_count(self):
        return self.call_count

if __name__ == "__main__":
    # Endereço e porta do servidor
    HOST = '127.0.0.1'
    PORT = 12345

    # Cria o servidor RPC
    server = SimpleXMLRPCServer((HOST, PORT), requestHandler=RequestHandler, logRequests=False)

    # Registra as funções RPC
    server.register_instance(RPCFunctions())

    print(f'Servidor RPC aguardando conexões em {HOST}:{PORT}')

    # Aceita conexões indefinidamente
    server.serve_forever()
