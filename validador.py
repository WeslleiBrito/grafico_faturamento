# coding: UTF-8
from datetime import date, datetime
from conexao_banco import conecta_banco


def valida_inteiro(valor):
    while True:
        try:
            valor = int(valor)
        except ValueError:
            valor = input('Informe um valor numérico válido: ')
        else:
            return int(valor)


def existe_nota(numero=0):
    banco = conecta_banco()
    cursor = banco.cursor()

    cursor.execute('SELECT nf FROM formacao_preco WHERE situacao ="0"')

    numeros = [int(num[0]) for num in cursor.fetchall()]

    if numero == 0 or numero in numeros:
        return True
    else:
        return 'Número não localizado ou nota já efetivada.'


def ultimo_dia_do_mes(mes=datetime.now().month, ano=datetime.now().year):
    """
    :param mes: Por padrão o mês ele é sempre um mês anterior ao atul
    :param ano: Por padrão ele sempre será o ano atual
    :return: retorna a última data do mês
    """

    for dia in range(31, -1, -1):

        try:
            return date(ano, mes, dia)
        except ValueError:
            continue


def valida_data(data: str):
    """
    :param data: Formato aceito ##/##/## ou ##/##/####
    :return: Caso seja uma data válida retorna a data já no padrão python, do contrario retorna false
    """
    try:
        return date.fromisoformat(str(data))
    except (ValueError, TypeError):
        raise 'Data inválida'


if __name__ == '__main__':
    print(valida_data('2022-09-30').month)
