def data_inicial_padrao(servidor='ServidorBalcao'):
    from conexao_banco import conecta_banco
    banco = conecta_banco(nome_host=servidor)
    cursor = banco.cursor()
    cursor.execute('SELECT rateio_dtvencimento FROM pagar_rateio')
    data = cursor.fetchall()[0][0]
    return data


def arredonda_float_duas_chaves(dicionario: dict):
    for chave in dicionario:
        for chave_valores in dicionario[chave]:
            if type(dicionario[chave][chave_valores]) == float:
                dicionario[chave][chave_valores] = round(dicionario[chave][chave_valores], 2)

    return dicionario


def arredonda_float_uma_chave(dicionario: dict):

    for valor in dicionario:
        if type(dicionario[valor]) is float:
            dicionario[valor] = round(dicionario[valor], 2)

    return dicionario


if __name__ == '__main__':
    print(data_inicial_padrao())
