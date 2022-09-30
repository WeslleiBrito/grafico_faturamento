from conexao_banco import conecta_banco
import re


def pega_numero_nota():
    banco = conecta_banco()
    cursor = banco.cursor()

    cursor.execute('SELECT receber_parcelas.parc_documento, receber.receb_agrupada, '
                   'receber.receb_obs FROM receber_parcelas INNER JOIN receber ON '
                   'receber_parcelas.parc_cod = receber.receb_cod INNER JOIN forma_pagamento '
                   'ON receber_parcelas.parc_forma = forma_pagamento.formpag_cod '
                   'WHERE receber.receb_agrupada = "S" AND receber.receb_dtemissao BETWEEN "2022-08-01" AND "2022-08-31"')
    tabela = cursor.fetchall()

    dicionario = {}
    for documento in tabela:
        dicionario[documento[0]] = []

    padrao = re.compile(r'Venda:  [0-9]{5}')

    for item in tabela:
        retornos = padrao.finditer(item[2])
        for retorno in retornos:
            inicio = retorno.span()[0]
            fim = retorno.span()[1] + 1
            dicionario[item[0]].append(int(item[2][inicio: fim][8:13]))

    for doc in dicionario.items():
        print(doc)


pega_numero_nota()
