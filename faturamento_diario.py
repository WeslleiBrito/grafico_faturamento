from lucratividade import Lucratividade
from rateio_despesa import DespesasRateio
from datetime import date


class FaturamentoDiario:

    def __init__(self):
        pass

    @property
    def faturamentoDiario(self):

        return self.__faturamentoDiario()

    def __faturamentoDiario(self):
        dados_faturamento = {}
        variavel = DespesasRateio().despesa_variavel

        for indice in range(date.today().day):
            dia = indice + 1
            mes = date.today().month
            ano = date.today().year

            if len(str(dia)) == 1:
                dia = f'0{dia}'

            if len(str(mes)) == 1:
                mes = f'0{mes}'

            valores = Lucratividade(data_inicial=f'{ano}-{mes}-{dia}', data_final=f'{ano}-{mes}-{dia}').totais
            dados_faturamento[f'{dia}/{mes}/{ano}'] = round(valores['faturamento'] - valores['faturamento'] * variavel,
                                                            2)

        return dados_faturamento
