# 38. Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros 
# números primos.
primo = []
naoPrimo = []
i = 0

num = int(input("Digite um numero inteiro positivo: "))
cont = num

if(num > 1):
    while(cont > 1):
        if(cont % num == 0):
            #Não Primo
            
            naoPrimo.append(cont)   
            print(cont)
            cont -= 1
        else:
            #Primo

            primo.append(cont)
            print(cont)
            cont -= 1


print(f"primo {primo}")
print(f"não primo {naoPrimo}")