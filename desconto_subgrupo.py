

class DescontoPorSubgrupo:
    def __init__(self):
        from faturamento_subgrupos import FaturamentoSubgrupo

        self.__faturamento = FaturamentoSubgrupo().faturamento_por_subgrupo

    @property
    def desconto_subgrupo(self):
        return self.__desconto_subgrupo()

    def __desconto_subgrupo(self):
        desconto_subgrupos = {}

        for subgrupo in self.__faturamento:
            faturamento = self.__faturamento[subgrupo]['faturamento']
            desconto = self.__faturamento[subgrupo]['desconto']

            if desconto > 0:
                calculo = round(desconto / (faturamento + desconto), 2)
            else:
                calculo = 0.15

            if calculo < 0.15:
                desconto_subgrupos[subgrupo] = 0.15
            else:
                desconto_subgrupos[subgrupo] = calculo

        return desconto_subgrupos


if __name__ == '__main__':
    descontos = DescontoPorSubgrupo().desconto_subgrupo
    print(descontos)
