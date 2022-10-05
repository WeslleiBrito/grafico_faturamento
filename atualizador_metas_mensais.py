# coding: UTF8

class AtualizaMetasGoogleDrive:

    def __init__(self, aba_tabela: str, codigo_planilha: str, caminho_chave: str):
        from resumo_mes import ResumosLucro

        self.__tabela = aba_tabela
        self.__codigo_planilha = codigo_planilha
        self.__caminho_chave = caminho_chave
        self.__resumo_lucro = ResumosLucro(comissao=1).resumo

    @property
    def atualizador_dados_meta(self):
        return self.__atualizador_dados_meta()

    @property
    def res(self):
        return self.__resumo_lucro

    def __conector_planilha(self):
        import gspread
        conecta_servico = gspread.service_account(self.__caminho_chave)
        return conecta_servico.open_by_key(self.__codigo_planilha).worksheet(self.__tabela)

    def __atualizador_dados_meta(self):
        planilha = self.__conector_planilha()
        
        legendas = ['Meta Vendas', 'Faturamento', 'Valor Meta Restante', 'Faturamento Real', 'Custo', 'Despesa Fixa',
                    'Lucro R$', 'Lucro %', 'Margem Real']

        for indice, chave in enumerate(legendas):
            if chave in legendas:
                planilha.update(f'A{indice + 2}', chave)
                planilha.update(f'B{indice + 2}', self.__resumo_lucro[chave])


if __name__ == '__main__':

    from atualizador_resumo_diario import AtualizaFaturamentoDiario
    aba = 'Dados'
    arquivo_chave = 'key.json'
    codigo_da_planilha = '1dbh8B_BrHkI_yrBgAEj8JnK0-5q2BQxn-25Ci-sKC4U'

    dados_gerais = AtualizaMetasGoogleDrive(aba_tabela=aba, caminho_chave=arquivo_chave,
                                            codigo_planilha=codigo_da_planilha).atualizador_dados_meta

    AtualizaFaturamentoDiario().atualizador_planilha_google