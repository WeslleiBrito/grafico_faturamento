# coding: UTF-8
import pandas as pd
import os
from colorama import Fore


class CriaNotaEntrada:

    def __init__(self, numero_nota=0, comissao=1, limite_desconto_lucro=0.3, caminho=''):
        from dados_sistema import DadosSistema
        from dados_fornecedor import DadosFornecedor
        from rateio_despesa import DespesasRateio

        if caminho:
            if not os.path.exists(caminho):
                try:
                    os.makedirs(caminho)
                    print(Fore.BLUE + 'Caminho do arquivo gerado automaticamente!' + Fore.RESET)
                    self.__caminho = caminho + '/'
                except PermissionError as err:
                    print(Fore.RED + f'Não foi permitodo a criação do arquivo: Erro {err}. {Fore.RESET}{Fore.BLUE}\nO documento será salvo no caminho: {os.getcwd()}\\Notas de Entrada' + Fore.RESET)
                    os.makedirs(os.getcwd() + '/Notas de Entrada', exist_ok=True)
                    self.__caminho = f'{os.getcwd()}/Notas de Entrada/'
            else:
                self.__caminho = caminho + '/'
        else:
            self.__caminho = caminho

        self.__dados_sistema = DadosSistema(numero_nota=numero_nota,
                                            limite_desconto_lucro=limite_desconto_lucro).dados_sistema
        self.__dados_fornecedor = DadosFornecedor(numero_nota=numero_nota).nota

        if comissao > 0:
            self.__comissao = comissao / 100
        else:
            self.__comissao = 0.01

        self.__despesa_variavel = DespesasRateio().despesa_variavel

    @property
    def nota_entrada(self):
        return self.__calcula_preco_venda()

    @property
    def caminho(self):
        return self.__caminho

    def __unifica_dados(self):
        return dict(self.__dados_fornecedor[0], **self.__dados_sistema)

    def __calcula_preco_venda(self):

        if type(self.__dados_fornecedor[0]) is dict and type(self.__dados_sistema) is dict:
            calulos_venda = {'despesa_variavel': [], 'valor_desconto': [], 'comissao': [], 'valor_lucro': [],
                             'venda': []}
            dados_unificados = self.__unifica_dados()

            for indice in range(len(self.__unifica_dados()['codigo'])):
                custo = dados_unificados['custo'][indice]
                despesa_fixa = dados_unificados['despesa_fixa'][indice]
                lucro = dados_unificados['lucro'][indice]
                desconto = dados_unificados['desconto'][indice]

                valor_monetario = custo + despesa_fixa
                valor_percentual = 1 - (self.__comissao + self.__despesa_variavel + desconto + lucro)
                preco_venda = round(valor_monetario / valor_percentual, 1)

                calulos_venda['despesa_variavel'].append(round(preco_venda * self.__despesa_variavel, 2))
                calulos_venda['valor_desconto'].append(round(preco_venda * desconto, 2))
                calulos_venda['comissao'].append(round(preco_venda * self.__comissao, 2))
                calulos_venda['valor_lucro'].append(round(preco_venda * lucro, 2))
                calulos_venda['venda'].append(preco_venda)

            return pd.DataFrame(dict(dados_unificados, **calulos_venda)).to_excel(
                f"{self.__caminho}{self.__dados_fornecedor[1]} {self.__dados_fornecedor[2]}.xlsx", sheet_name='Compra')

        return Fore.RED + 'Nota não localizada ou finalizada' + Fore.RESET


if __name__ == '__main__':
    nota_entrada = CriaNotaEntrada(caminho=r'C:/Users/9010/Desktop/Criação de preços')
    nota = nota_entrada.nota_entrada
    print(Fore.GREEN + 'Nota criada com sucesso em:' + Fore.RESET, nota_entrada.caminho)
