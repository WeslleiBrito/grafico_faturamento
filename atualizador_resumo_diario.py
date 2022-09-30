# coding: UTF-8

class AtualizaFaturamentoDiario:
    def __init__(self):
        from lucratividade import Lucratividade
        self.__faturamento = Lucratividade(comissao=1).totais

    @property
    def conecta(self):
        return self.__conector_planilha()

    @property
    def atualizador_planilha_google(self):
        return self.__atualizador_planilha_google()

    def __conector_planilha(self):
        import gspread
        conecta_servico = gspread.service_account('key.json')
        return conecta_servico.open_by_key('1dbh8B_BrHkI_yrBgAEj8JnK0-5q2BQxn-25Ci-sKC4U'). \
            worksheet('Faturamento Diário')

    def __atualizador_planilha_google(self):
        planilha = self.__conector_planilha()
        faturamento = self.__faturamento
        print(faturamento)
        for indice, chave in enumerate(faturamento):
            planilha.update(f'B{indice + 2}', faturamento[chave])


if __name__ == '__main__':
    AtualizaFaturamentoDiario().atualizador_planilha_google
