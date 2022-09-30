import plotly.graph_objects as go
from resumo_mes import ResumosLucro
from main import faturamentos
from rateio_despesa import DespesasRateio

despesa_variavel = DespesasRateio().despesa_variavel

dados = faturamentos(comissao=1)
valores_faturamento = dados[0]
soma_faturamento = []
meta_restante = []
vr = 0
for valor in valores_faturamento:
    vr += valor
    soma_faturamento.append(vr)

datas = dados[1]
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

fig.add_trace(go.Scatter(x=datas, y=lista_meta, name='Meta', mode='lines + markers', fillcolor='red'))
fig.add_trace(go.Scatter(x=datas, y=soma_faturamento, name='Faturamento', mode='lines + markers'))
fig.add_trace(go.Scatter(x=datas, y=meta_restante, name='Meta Restante', mode='lines + markers'))

fig.update_layout(title='Faturamento x Meta x Meta Restante',
                  xaxis_title='Datas',
                  yaxis_title='Faturamento(Datas)',
                  plot_bgcolor='black',
                  font={'family': 'Arial', 'size': 16, 'color': 'black'})
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray',
                 showline=True, linewidth=1, linecolor='white')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray',
                 showline=True, linewidth=1, linecolor='white')

fig.show()
