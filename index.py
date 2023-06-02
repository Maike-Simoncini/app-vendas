print('Bem vindo a loja do Maike Simoncini da Silva') # identificador pessoal
valor_produto = float(input('Entre com valor do produto: ')) # entrada valor do produto
quant_produto = int(input('Entre com valor da quantidade: ')) # entrada quantidade do produto
desconto_produto = 0 # variável desconto
# desconto por quantidade de produto
if quant_produto <= 9: 
  desconto_produto = 0.00 # 0% de desconto
elif quant_produto >= 10 and quant_produto <= 99: 
  desconto_produto = 0.05 # 5% de desconto
elif quant_produto >= 100 and quant_produto <= 999: 
  desconto_produto = 0.10 # 10% de desconto
else: 
  desconto_produto = 0.15 # 15% de desconto
total_desconto = int(desconto_produto * 100)
total_sem_desconto = valor_produto * quant_produto # variável total de produto sem desconto
print('O valor sem desconto foi: R$ {:.2f}'.format(total_sem_desconto)) # saída do total sem desconto
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto # variável total de produto com desconto
print('O valor com desconto foi: R$ {:.2f} (desconto {}%)'.format(total_com_desconto,total_desconto)) # saída total com desconto
