import plotly.graph_objects as go
from resumo_mes import ResumosLucro
from main import faturamentos
from rateio_despesa import DespesasRateio
from numero_formato_brasileiro import conversor_de_moeda

despesa_variavel = DespesasRateio().despesa_variavel

dados = faturamentos(comissao=1)
valores_faturamento = dados[0]
datas = dados[1]
comissao = dados[2]
soma_faturamento = []
meta_restante = []
vr = 0

for valor in valores_faturamento:
    vr += valor * (1 - (despesa_variavel + comissao))
    soma_faturamento.append(vr)



meta_geral = ResumosLucro(comissao=1).resumo['Meta Vendas']
lista_meta = [meta_geral for meta in range(len(datas))]

meta_atual = meta_geral

for faturamentos in valores_faturamento:
    meta_atual -= faturamentos
    if meta_atual >= 0:
        meta_restante.append(round(meta_atual, 2))
    else:
        meta_restante.append(0.00)

fig = go.Figure()

fig.add_trace(go.Scatter(x=datas, y=lista_meta, name=f'Meta: {conversor_de_moeda(meta_geral)}', mode='lines + markers'))
fig.add_trace(go.Scatter(x=datas, y=soma_faturamento, name=f'Faturamento: {conversor_de_moeda(round(vr, 2))}', mode='lines + markers'))
fig.add_trace(go.Scatter(x=datas, y=meta_restante, name=f'Meta Restante: {conversor_de_moeda(meta_restante[-1])}', mode='lines + markers'))


fig.update_layout(title='Faturamento x Meta x Meta Restante',
                  xaxis_title='Datas',
                  yaxis_title='Faturamento(Datas)',
                  plot_bgcolor='white',
                  font={'family': 'Arial', 'size': 16, 'color': 'black'})
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray',
                 showline=True, linewidth=1, linecolor='black')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray',
                 showline=True, linewidth=1, linecolor='black')

fig.show()
