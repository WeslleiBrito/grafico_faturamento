from conexao_banco import conecta_banco

banco = conecta_banco()
cursor = banco.cursor()

cursor.execute('SELECT venda.total FROM `venda` WHERE venda.`data` BETWEEN "2022-09-26" and "2022-09-26"')

total = sum([total[0] for total in cursor.fetchall()])

print(total)