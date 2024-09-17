venda = float(input("Digite o valor da venda: $ "))
desconto_venda = venda * 0.10
total_venda = venda - desconto_venda 
valor_parcela = venda / 3 
comissao_avista = desconto_venda * 0.05
comissao_parcelado = valor_parcela * 0.05

print("O total a pagar com desconto de 10% é de: $", total_venda ,
      "\nO valor de cada parcela, no parcelamento de 3X sem juros é de: $", valor_parcela ,
      "\nA comissão do vendedor, no caso da venda ser a vista (5% Sobre o valor com desconto) é de: $" , comissao_avista,
      "\nA comissão do vendedor, no caso da venda ser parcelada (5% Sobre o valor total) ",comissao_parcelado ,
)