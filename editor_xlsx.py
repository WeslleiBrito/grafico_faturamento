# coding: UTF-8
from openpyxl import load_workbook
from openpyxl.styles import Side, Border, NamedStyle, Font, Alignment
from lucratividade import Lucratividade
from resumo_lucratividade import CriaPlanilhaLucratividadeItem

lucratividades = Lucratividade(comissao=1)
dicionario_lucratividade_item = lucratividades.lucratividade_por_item
totais = lucratividades.totais

planilha_base = CriaPlanilhaLucratividadeItem(dicionario_lucratividade_item).dicionario_lista


planilha_modelo = load_workbook('modelo_lucro_item.xlsx')
data = lucratividades.data_de_consulta

bordas = Side(border_style="thin", color="000000")
valores = []
fonte = NamedStyle(name='Calibri')
fonte.font = Font(bold=True, size='11')

colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
indice_valores = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11]

faturamento = 0.0
custo = 0.0
comissao = 0.0
custo_despesa = 0.0
lucro = 0.0
percentual = 0.0
linha_final = 5

for index, dados in enumerate(planilha_base.values):
    linha_final += index

    for indice, coluna in zip(indice_valores, colunas):
        planilha_modelo['Relatório'][f'{coluna}{index + 2}'] = dados[indice]
        planilha_modelo['Relatório'][f'{coluna}{index + 2}'].style = fonte
        planilha_modelo['Relatório'][f'{coluna}{index + 2}'].alignment = Alignment(horizontal="center",
                                                                                   vertical="center")
        planilha_modelo['Relatório'][f'{coluna}{index + 2}'].border = Border(top=bordas, left=bordas, right=bordas,
                                                                             bottom=bordas)

index += 5
planilha_modelo['Relatório'][f'G{index}'] = 'Faturamento'
planilha_modelo['Relatório'][f'H{index}'] = totais['faturamento']
planilha_modelo['Relatório'][f'G{index + 1}'] = 'Custo'
planilha_modelo['Relatório'][f'H{index + 1}'] = totais['custo']
planilha_modelo['Relatório'][f'G{index + 2}'] = 'Comissão'
planilha_modelo['Relatório'][f'H{index + 2}'] = totais['comissao']
planilha_modelo['Relatório'][f'G{index + 3}'] = 'CMV+Despesa'
planilha_modelo['Relatório'][f'H{index + 3}'] = totais['custo'] + totais['comissao'] + totais['despesa fixa'] + totais['despesa variavel']
planilha_modelo['Relatório'][f'G{index + 4}'] = 'Lucro R$'
planilha_modelo['Relatório'][f'H{index + 4}'] = totais['lucro']

if totais['lucro'] and totais['faturamento'] != 0:
    planilha_modelo['Relatório'][f'G{index + 5}'] = 'Lucro %'
    planilha_modelo['Relatório'][f'H{index + 5}'] = round(totais['lucro'] / totais['faturamento'], 2) * 100

planilha_modelo.save(rf'C:\Users\9010\Desktop\Relatório de Lucratividade\lucratividade_{data}.xlsx')
