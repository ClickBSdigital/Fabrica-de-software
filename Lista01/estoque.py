#p1=produto de entrada q1=quantidade v1=valor de entrada v2=valor de saída
produto = input("DIGITE NOME DO PRODUTO: ")
quantidade_entrada = int(input("DIGITE A QUANTIDADE DE ENTRADA: "))
quantidade_saida = int(input("DIGITE A QUANTIDADE DE SAÍDA: "))
codigo_do_produto = float(input("DIGITE O CÓDIGO DO PRODUTO: "))
valor_entrada = float(input("DIGITE O VALOR DE ENTRADA: "))
valor_saida = float(input("DIGITE VALOR DE SAÍDA: "))

res1 = valor_saida - valor_entrada 
print("\n O VALOR DE LUCRO É: ", res1)

estoque = quantidade_entrada + quantidade_entrada
print("\n A QUANTIDADE EM ESTOQUE É: ", estoque)

res2 = quantidade_saida % quantidade_entrada
print("\n A QUANTIDADE DE PRODUTOS É: ", res2 )
