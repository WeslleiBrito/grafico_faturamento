from rateio_despesa import DespesasRateio

def faturamentos(despesa_variavel=DespesasRateio().despesa_variavel, comissao=0):

    from datetime import date
    from tqdm import trange
    from conexao_banco import conecta_banco

    if comissao > 0:
        comissao /= 100

    banco = conecta_banco()
    cursor = banco.cursor()
    data_atual = date.today()
    datas = []
    fats = []

    for dia in trange((data_atual.day - date(data_atual.year, data_atual.month, 1).day) + 1):
        ano = data_atual.year
        mes = data_atual.month
        if len(str(mes)) < 2:
            mes = f'0{mes}'

        dia += 1
        if len(str(dia)) < 2:
            dia = f'0{dia}'


        comando = f'SELECT venda_item.qtd, venda_item.qtd_devolvida, venda_item.total FROM venda_item WHERE venda_item.dtvenda BETWEEN "{ano}-{mes}-{dia}" and "{ano}-{mes}-{dia}";'
        cursor.execute(comando)

        faturamento_unitario = []
        for item in cursor.fetchall():
            if float(item[0]) - float(item[1]) > 0:
                faturamento_unitario.append((float(item[2]) / float(item[0])) * (float(item[0]) - float(item[1])))
        valor_faturado = round(sum(faturamento_unitario), 2)
        fats.append(valor_faturado)
        datas.append(f'{dia}-{mes}-{ano}')
        faturamento_unitario.clear()

    return fats, datas, comissao


if __name__ == '__main__':
    print(faturamentos(comissao=1))
