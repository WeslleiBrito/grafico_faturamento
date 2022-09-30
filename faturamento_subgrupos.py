# coding: UTF-8
from conexao_banco import conecta_banco
from valores_padroes import data_inicial_padrao
from datetime import date
from validador import valida_data


class FaturamentoSubgrupo:
    def __init__(self, data_inicial='', data_final=''):
        self.__banco = conecta_banco()
        self.__cursor = self.__banco.cursor()

        if data_inicial == '':
            self.__data_inicial = data_inicial_padrao()
        else:
            self.__data_inicial = valida_data(data_inicial)

            if self.__data_inicial > date.today():
                self.__data_inicial = date.today()

        if data_final == '':
            self.__data_final = date.today()
        else:
            self.__data_final = valida_data(data_final)

            if self.__data_inicial > self.__data_final:
                self.__data_final = self.__data_inicial


    @property
    def faturamento_por_subgrupo(self):
        return self.__faturamento_subgrupo()

    @property
    def datas(self):
        return self.__data_inicial, self.__data_final

    @property
    def faturamento_total(self):
        return self.__faturamento_total()

    @property
    def custo_total(self):
        return self.__custo_total()

    def __soma_produtos(self):

        self.__cursor.execute(
            f'SELECT produto, SUM(qtd - qtd_devolvida), SUM(vrcusto_composicao * (qtd - qtd_devolvida)), SUM(desconto), SUM(total), SUM(qtd_devolvida)  FROM venda_item WHERE dtvenda BETWEEN "{self.__data_inicial}" AND "{self.__data_final}" GROUP BY descricao ORDER BY total DESC;')

        valores = self.__cursor.fetchall()

        return [(dados[0], dados[1], dados[2], float(dados[3]), float(dados[4]), dados[5]) for dados in valores]

    def __lista_subgrupos(self):
        self.__cursor.execute('SELECT subprod_descricao FROM subgrupo_produtos')

        return [descricao[0] for descricao in self.__cursor.fetchall()]

    def __faturamento_subgrupo(self):
        self.__cursor.execute("SELECT prod_cod, prod_dsubgrupo FROM produto")

        codigo_subgrupo = self.__cursor.fetchall()
        codigos = [cod[0] for cod in codigo_subgrupo]
        subgrupo_lista = [sub[1] for sub in codigo_subgrupo]

        subgrupo = dict()

        for nome in self.__lista_subgrupos():
            subgrupo[nome] = {'quantidade': 0.0, 'custo': 0.0, 'desconto': 0.0,
                              'faturamento': 0.0, 'qtd_devolvida': 0.0}

        for item in self.__soma_produtos():
            chave = subgrupo_lista[codigos.index(item[0])]
            subgrupo[chave]['quantidade'] += item[1]
            subgrupo[chave]['custo'] += item[2]
            subgrupo[chave]['desconto'] += item[3]
            subgrupo[chave]['faturamento'] += item[4]
            subgrupo[chave]['qtd_devolvida'] += item[5]

        return subgrupo

    def __faturamento_total(self):
        geral = self.__faturamento_subgrupo()
        return round(sum([geral[item]['faturamento'] for item in geral]), 2)

    def __custo_total(self):
        geral = self.__faturamento_subgrupo()
        return round(sum([geral[item]['custo'] for item in geral], 2))


if __name__ == '__main__':
    fatura = FaturamentoSubgrupo()
    print(fatura.faturamento_por_subgrupo)
