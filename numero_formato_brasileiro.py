
def conversor_de_moeda(valor):
	s_valor = list(f'{valor:,.2f}'.replace('.', ','))

	for poicao, digito in enumerate(s_valor[:-3]):
		if digito == ',':
			s_valor[poicao] = '.'

	return ''.join(s_valor)
