# coding: UTF-8
from faturamento_subgrupos import FaturamentoSubgrupo
from despesas import Despesas


class DespesaSubgrupo:

    def __init__(self):
        self.__fatura_subgrupo = FaturamentoSubgrupo().faturamento_por_subgrupo
        self.__faturamento_total = FaturamentoSubgrupo().faturamento_total
        self.__despesa_fixa_total = Despesas().fixa
        self.__despesa_variavel_total = Despesas().variavel

    @property
    def despesa_fixa_subgrupo(self):
        return self.__despesa_fixa_subgrupo()

    @property
    def despesa_variavel(self):
        return self.__despesa_variavel()

    def __despesa_fixa_subgrupo(self):
        despesa_subgrupo = dict()

        for item in self.__fatura_subgrupo:
            faturamento_subgrupo = self.__fatura_subgrupo[item]['faturamento']
            quantidade = self.__fatura_subgrupo[item]['quantidade']
            if faturamento_subgrupo:
                despesa_subgrupo[item] = round(((faturamento_subgrupo / self.__faturamento_total) * self.__despesa_fixa_total) / quantidade, 2)
            else:
                despesa_subgrupo[item] = 0.0

        return despesa_subgrupo

    def __despesa_variavel(self):
        return round(self.__despesa_variavel_total / self.__faturamento_total, 2)


if __name__ == '__main__':
    print(DespesaSubgrupo().despesa_fixa_subgrupo)
