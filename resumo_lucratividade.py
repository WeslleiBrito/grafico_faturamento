# coding: UTF-8
class CriaPlanilhaLucratividadeItem:

    def __init__(self, dicionario: dict):
        self.__dicionario = dicionario

    @property
    def dicionario_lista(self):
        return self.__dicionario_lista()

    def __dicionario_lista(self):
        import pandas as pd
        from datetime import date

        venda = []
        vendedor = []
        quantidade = []
        descricao = []
        custo = []
        despesa_fixa = []
        despesa_variavel = []
        comissao = []
        custo_total = []
        faturamento = []
        lucro = []
        porcentagem = []

        for produtos in self.__dicionario.values():
            for valores in produtos:
                venda.append(valores['venda'])
                vendedor.append(valores['vendedor'])
                quantidade.append(valores['quantidade'])
                descricao.append(valores['descricao'])
                custo.append(valores['custo'])
                despesa_fixa.append(valores['despesa fixa'])
                despesa_variavel.append(valores['despesa variavel'])
                comissao.append(valores['comissao'])
                custo_total.append(valores['custo total'])
                faturamento.append(valores['faturamento'])
                lucro.append(valores['lucro'])

                if valores['lucro'] != 0:
                    porcentagem.append(valores['porcentagem'])

        data = str(date.today())
        data = f'{data[8:]}-{data[5:7]}-{data[0:4]}'

        return pd.DataFrame(
            {'Nº': venda, 'Vendedor': vendedor, 'Qtd': quantidade, 'Descrição': descricao, 'Custo': custo,
             'D. Fixa': despesa_fixa, 'D.Variável': despesa_variavel, 'Comissão': comissao,
             'Total': custo_total, 'Faturamento': faturamento, 'Lucro R$': lucro,
             'Lucro %': porcentagem})


if __name__ == '__main__':
    from lucratividade import Lucratividade

    dicionario_lucratividade_item = Lucratividade(comissao=1).lucratividade_por_item
    dc = CriaPlanilhaLucratividadeItem(dicionario_lucratividade_item).dicionario_lista

