import socket


def busca_ip(nome_maquina):
    try:
        return socket.gethostbyname(nome_maquina)
    except socket.error as erro:
        raise NameError(f"Verifique o nome do host informado: {erro}")


if __name__ == '__main__':
    print(busca_ip('ServidorBalcao'))
