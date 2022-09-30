from conecta_banco import BancoDeDados
from datetime import datetime
from math import floor


def calcula_meses():
    inicio_contagem = datetime.strptime('2020-08-01', '%Y-%m-%d')

    fim_contagem = datetime.strptime(str(datetime.today().date()), '%Y-%m-%d')

    quantidade_dias = abs((fim_contagem - inicio_contagem)).days

    return floor(quantidade_dias / 30)


def registra_despesa_geral():
    fixa = 0.00
    variavel = 0.0
    meses = calcula_meses()

    banco = BancoDeDados().banco
    cursor = banco.cursor_sqlite()

    tipo_despesa = [tipo[0] for tipo in cursor.execute('SELECT tipo_despesa FROM despesas_totais').fetchall()]
    valor_despesa = [despesa[0] for despesa in cursor.execute('SELECT valor FROM despesas_totais').fetchall()]
    faturamento = cursor.execute('SELECT faturamento FROM valores_gerais').fetchall()[0]

    for posicao, tipo in enumerate(tipo_despesa):
        if tipo == 'Fixa':
            fixa += valor_despesa[posicao]
        else:
            variavel += valor_despesa[posicao]

    fixa_mensal = round(fixa / meses)
    variavel_mensal = round(variavel / meses)
    variavel_percentual = round(variavel / faturamento[0], 2)

    if cursor.execute(f'SELECT indice FROM valores_gerais WHERE indice = 1').fetchall():
        cursor.execute(
            f'UPDATE valores_gerais SET despesa_fixa_total = {fixa}, despesa_variavel_total = {variavel}, '
            f'numero_meses = {meses}, despesa_fixa_mensal = {fixa_mensal}, despesa_variavel_mensal = {variavel_mensal}, despesa_variavel_percentual = {variavel_percentual} WHERE indice = 1')
    else:
        cursor.execute(
            f'INSERT INTO valores_gerais (despesa_fixa_total, despesa_variavel_total, despesa_variavel_mensal, despesa_fixa_mensal, despesa_variavel_percentual, numero_meses) VALUES (?, ?, ?)',
            (fixa, variavel, fixa_mensal, variavel_mensal, variavel_percentual, meses))
    banco.commit()


if __name__ == '__main__':
    print(calcula_meses())
