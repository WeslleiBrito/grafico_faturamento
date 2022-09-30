from faturamento_subgrupos import FaturamentoSubgrupo
from despesas import Despesas


class DespesasRateio:
    def __init__(self):
        self.__faturamento = FaturamentoSubgrupo().faturamento_por_subgrupo
        self.__despesa_fixa = Despesas().fixa
        self.__despesa_variavel = Despesas().variavel

    @property
    def despesa_fixa(self):
        return self.__calcula_despesa_fixa()

    @property
    def despesa_variavel(self):
        return self.__calculo_despesa_variavel()

    def __calculo_despesa_variavel(self):
        faturamento_total = sum([venda['faturamento'] for venda in self.__faturamento.values()])

        return round(self.__despesa_variavel / faturamento_total, 2)

    def __calcula_despesa_fixa(self):
        despesa_subgrupo = dict()
        faturamento_total = sum([venda['faturamento'] for venda in self.__faturamento.values()])

        for fatura in self.__faturamento:
            if self.__faturamento[fatura]['faturamento'] > 0:
                calculo = (self.__faturamento[fatura]['faturamento'] / faturamento_total) * self.__despesa_fixa / \
                          self.__faturamento[fatura]['quantidade']
                despesa_subgrupo[fatura] = round(calculo, 2)
            else:
                despesa_subgrupo[fatura] = 0.0

        return despesa_subgrupo


if __name__ == '__main__':
    print(DespesasRateio().despesa_variavel)
