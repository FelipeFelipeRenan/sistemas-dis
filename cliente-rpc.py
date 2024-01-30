import xmlrpc.client

# Endereço do servidor
endereco_servidor = 'http://localhost:21212'

# Criar proxy para se comunicar com o servidor
proxy = xmlrpc.client.ServerProxy(endereco_servidor)

# Teste das funções remotas
print(proxy.armazenar_mensagem("Olá, servidor! Esta é uma mensagem de teste."))
print(proxy.recuperar_mensagens())
print(proxy.obter_ip_servidor())
print(proxy.obter_data_hora_servidor())
