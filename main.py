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

        cursor.execute \
            (f'SELECT venda.total FROM `venda` WHERE venda.`data` BETWEEN "{ano}-{mes}-{dia}" and "{ano}-{mes}-{dia}"')

        faturamento = round(sum([total[0] for total in cursor.fetchall()]) * (1 - (despesa_variavel + comissao)), 2)
        fats.append(faturamento)
        datas.append(f'{dia}-{mes}-{ano}')

    return fats, datas


if __name__ == '__main__':
    print(faturamentos())
