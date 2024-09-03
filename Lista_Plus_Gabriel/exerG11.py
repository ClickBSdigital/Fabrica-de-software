# Escreva  um  programa  que  peça  ao  usuário  para  digitar  uma  senha.  O 
# programa deve continuar pedindo a senha até que o usuário digite 
# corretamente a senha "python123". Quando a senha for correta, o programa 
# deve imprimir "Acesso concedido!" e encerrar. 

senha = 'python123'

while(True):
    acesso = input("Digite a senha: ")

    if(acesso == senha):
        print("acesso concedido!")
        break
    else:
        print("Acesso negado:")