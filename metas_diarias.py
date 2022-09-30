class MetasDiarias:

    def __init__(self):
        from feriado import feriados
        from valores_padroes import data_inicial_padrao
        import datetime as dt
        from dias_uteis import networkdays
        from despesas import Despesas

        self.__feriados = feriados(country='BR', state='BA', data_inicial=data_inicial_padrao().year,
                                   data_final=dt.datetime.today().year + 1)

        self.__dias_uteis = networkdays(start_date=data_inicial_padrao(), end_date=dt.date.today())

        self.__despesa_fixa = Despesas().fixa
        self.__despesa_variavel = Despesas().variavel

    @property
    def despesa_fixa(self):
        return self.__meta_fixa()

    @property
    def despesa_variavel(self):
        return self.__meta_variavel()

    def __meta_fixa(self):
        return round(self.__despesa_fixa / (self.__dias_uteis - self.__feriados), 2)

    def __meta_variavel(self):
        return round(self.__despesa_variavel / (self.__dias_uteis - self.__feriados), 2)


if __name__ == '__main__':
    print(MetasDiarias().despesa_fixa)
    print(MetasDiarias().despesa_variavel)
