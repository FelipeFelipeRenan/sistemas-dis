from xmlrpc.client import ServerProxy

def main():
    # Cria um proxy para o servidor RPC local
    local_proxy = ServerProxy("http://localhost:12345/RPC2")

    # Chama a função para obter a data e hora atual localmente
    current_datetime_local = local_proxy.get_current_datetime()
    print(f'Data e Hora Local: {current_datetime_local}')

    # Chama a função para obter a quantidade de chamadas localmente
    call_count_local = local_proxy.get_call_count()
    print(f'Quantidade de Chamadas Local: {call_count_local}')

    # Cria um proxy para o servidor RPC remoto
    remote_proxy = ServerProxy("http://endereco_do_servidor_remoto:12345/RPC2")

    # Chama a função para obter a data e hora atual remotamente
    current_datetime_remote = remote_proxy.get_current_datetime()
    print(f'Data e Hora Remota: {current_datetime_remote}')

    # Chama a função para obter a quantidade de chamadas remotamente
    call_count_remote = remote_proxy.get_call_count()
    print(f'Quantidade de Chamadas Remota: {call_count_remote}')

if __name__ == "__main__":
    main()
