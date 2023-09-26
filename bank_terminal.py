# Criar terminal bancário com apenas 3 opções:
# 1 - Saldo 2 - Saque 3 - Depósito;
# Verificar condições de saque e depósito;
# valor máximo de saque: 500;
# limite de saques: 3;
# função saldo deve listar todos os saques e depósitos feitos na conta e retornar valor final do saldo. Ex. R$ 1500.45

menu = int(input("Digite a opção desejada: \n [1] Saldo \n [2] Saque \n [3] Depósito \n [0] Sair \n"))

saldo = 0
saque = 0
deposito = 0
limite_saque = 3
valor_maximo_saque = 500
valor_maximo_deposito = 1000

while menu != 0:
    if menu == 1:
        print("==============EXTRATO==============")
        print("Não há movimentações na conta!" if not saldo else saldo)
        print("Saldo: R$", saldo)
        print("===================================")
    elif menu == 2:
        if limite_saque > 0:
            saque = float(input("Informe o valor do saque: "))
            if saque <= valor_maximo_saque:
                saldo = saldo - saque
                limite_saque = limite_saque - 1
                print("Saque autorizado!")
            else:
                print("Valor máximo de saque excedido!")
        else:
            print("Limite de saques excedido!")
    elif menu == 3:
        deposito = float(input("Informe o valor do depósito: "))
        if deposito <= valor_maximo_deposito:
            saldo = saldo + deposito
            print("Depósito realizado com sucesso!")
        else:
            print("Valor máximo de depósito excedido!")
    else:
        print("Opção inválida!")
    menu = int(input("Digite a opção desejada: \n [1] Saldo \n [2] Saque \n [3] Depósito \n [0] Sair \n"))
else:
    print("Obrigado por utilizar nossos serviços!")