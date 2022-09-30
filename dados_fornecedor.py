import datetime


class DadosFornecedor:

    def __init__(self, numero_nota=0):
        from conexao_banco import conecta_banco
        from validador import existe_nota
        self.__valida_numero_nota = existe_nota(numero=numero_nota)
        self.__banco = conecta_banco()
        self.__cursor = self.__banco.cursor()
        self.__numero_nota = numero_nota

    @property
    def nota(self):
        return self.__dados_fornecedor()

    @property
    def todas_as_notas(self):
        return self.__notas_abertas()

    def __notas_abertas(self):
        self.__cursor.execute("""select 
N.numero Num_NF, 
N.emi_razao Fornecedor,
DATE_FORMAT(N.dtentrada,'%d%/%m%/%Y') Data,
I.nitem Item,
P.prod_cod Codigo,
P.prod_descricao,
I.und UN,
I.qtdestoque Qtd_Estoque,
I.vrcompra Vr_compra,
I.pcustos Perc_custo,
I.vrcompra Vr_Custo,
I.margem Margem,
I.vrvenda Vr_Venda,
I.pdescmax Desconto_max,
I.vrcusto_medio,
I.qtdentrada,
I.vrcompra_novo,
I.vrcustoagregado,
I.fracao,
I.custo vr_Compra_fracionado,
I.pcusto_nota Perc_custo_NF,
I.vrvenda_novo
from formacao_preco F
inner join formacao_itens I on F.codigo = I.formacao
inner join produto P on P.prod_cod = I.produto
INNER JOIN nfc N ON n.nfc_codigo = F.nf_codigo
WHERE N.`status` = 'F' and F.situacao = "0"
order by F.codigo, I.nitem
""")

        return self.__cursor.fetchall()

    def __dados_fornecedor(self):

        if type(self.__valida_numero_nota) is bool:
            # armazenando todas as notas em aberto
            notas = self.__notas_abertas()

            # pegando todos numeros das notas colocando em um set em seguida salvando dentro da lista já convertida para inteiro
            numeros_notas = [(int(num[0]), num[1]) for num in set([(numero[0], numero[2]) for numero in notas])]

            # pegando todas as data colocando em um set em seguida salvando dentro da lista
            datas = [data[1] for data in numeros_notas]

            # transformando as datas do tipo string em datas do tipo data
            if datas:
                for posicao, item in enumerate(datas):
                    ano = int(item[6:])
                    mes = int(item[3:5])
                    dia = int(item[0:2])
                    datas[posicao] = datetime.date(ano, mes, dia)

            # pegando a ultima data e convertendo ela para string
            ultima_data = str(max(datas))

            # editando o formato da última data para fazer comparações com as datas das notas
            data_formatada = f'{ultima_data[8:]}/{ultima_data[5:7]}/{ultima_data[0:4]}'

            # variavel de verificação de extistencia da nota no sistema, por padrão false
            testa_numero_nota = False

            # inicializando variavel
            num_nota = 0

            # inicializando dicionário da nota
            nota = {'codigo': [], 'quantidade': [], 'descricao': [], 'custo': []}

            if self.__numero_nota == 0:
                for valor in numeros_notas:
                    # verificando se a data é a última data, caso seja atribui o numero a nota
                    if valor[1] == data_formatada:
                        num_nota = valor[0]
            else:
                num_nota = self.__numero_nota

            fornecedor = ''
            if num_nota:
                for item in notas:
                    if int(item[0]) == num_nota:
                        nota['codigo'].append(item[4])
                        nota['quantidade'].append(float(item[15]) * float(item[18]))
                        nota['descricao'].append(item[5])
                        nota['custo'].append(float(item[19]))
                        if len(item[1]) > 15:
                            fornecedor = str(item[1][0:16])
                        else:
                            fornecedor = str(item[1])

                        for caract in fornecedor:
                            if not caract.isalpha():
                                fornecedor = fornecedor.replace(f'{caract}', ' ')

                return nota, fornecedor, num_nota


if __name__ == '__main__':
    nfc = DadosFornecedor().nota
    print(nfc)
