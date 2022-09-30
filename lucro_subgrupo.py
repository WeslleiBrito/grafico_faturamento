

class LucroSubgrupo:
    def __init__(self):
        from conexao_banco import conecta_banco

        self.__banco = conecta_banco()
        self.__cursor = self.__banco.cursor()

    @property
    def lucro_por_subgrupo(self):
        return self.__lucro_por_subgrupo()

    def __lucro_por_subgrupo(self):
        self.__cursor.execute('SELECT subprod_descricao, plucro FROM subgrupo_produtos')
        tabela = self.__cursor.fetchall()
        dict_lucro_subgrupo = {}

        for item in tabela:
            dict_lucro_subgrupo[item[0]] = round(item[1] / 100, 2)

        return dict_lucro_subgrupo


if __name__ == '__main__':
    lc_subgrupos = LucroSubgrupo().lucro_por_subgrupo
    print(lc_subgrupos)
