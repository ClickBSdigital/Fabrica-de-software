# t1 = ('Doce', 2.3, 'Bala ', 0.15, 'Pizza ', 28.9, 'Arroz ', 4.5, 'Paçoca ', 0.5, 'Pamonha', 5.4)

# pontos = ('-'*30)
# print(pontos)
# print('-'*10,'CARDÁPIO','-'*10)
# print(pontos)

# for i in range(len(t1)):
#  print(t1[i])
# print()

# carrinho = input("Digite a sua escolha do cardápio: ")
# mais_itens = input("Você quer continuar a adicionar mais itens? (s/n): ")

# soma = 0

# while mais_itens == 's':

#  carrinho = input("Digite a sua escolha do cardápio: ")
#  mais_itens = input("Você quer continuar a adicionar mais itens? (s/n): ")


#  if carrinho == 'Doce':
#    soma = t1[1]
   
#  elif carrinho == 'Bala':
#    soma = t1[3]
   
#  elif carrinho == 'Pizza':
#    soma = t1[5]
   
#  elif carrinho == 'Arroz':
#    soma = t1[7]
   
#  elif carrinho == 'Paçoca':
#    soma = t1[9]
   
#  elif carrinho == 'Pamonha':
#      soma = t1[11]

# print('O valor total da sua conta é: R${}.'.format(soma))

t1 = ('Doce', 2.3, 'Bala ', 0.15, 'Pizza ', 28.9, 'Arroz ', 4.5, 'Paçoca ', 0.5, 'Pamonha', 5.4)
print('-'*30)
print(f'{"Cardápio":^30}')
print('-'*30)
for pos in range(0,len(t1)):
  if pos % 2 == 0:
    print(f'{t1[pos]:.<20}', end='')
  else:
    print(f'R${t1[pos]:>6.2f}')
print('-'*30)

soma = 0
i = 0
mais = 's'

while mais == 's':

  carrinho = input("Digite a sua escolha do cardápio: ")
 
  if carrinho == 'Doce' or carrinho == 'doce':
    i = t1[1]
   
  elif carrinho == 'Bala':
    i = t1[3]
   
  elif carrinho == 'Pizza':
    i = t1[5]
   
  elif carrinho == 'Arroz':
    i = t1[7]
   
  elif carrinho == 'Paçoca':
    i = t1[9]
   
  elif carrinho == 'Pamonha':
    i = t1[11]  

  soma = soma + i
  mais = input("Você quer continuar a adicionar mais itens? (s/n): ")

print(f"O valor total da sua conta é: R${soma}.")