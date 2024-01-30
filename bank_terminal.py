import textwrap

def menu():
    menu = """\n
    =============== BANCO PYTHON ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    ============================================
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de\t R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===\n")
        
    else:
        print("\n=== Valor inválido! ===\n")
        
    return saldo, extrato    
        
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n=== Saldo insuficiente! ===\n")
        
    elif excedeu_limite:
        print("\n=== Limite de saque excedido! ===\n")
        
    elif excedeu_saques:
        print("\n=== Limite de saques excedido! ===\n")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===\n")
        
    else: 
        print("\n=== Valor inválido! ===\n")
        
    return saldo, extrato, numero_saques                    

def exibir_extrato(saldo, /, *, extrato):
    print("\n============== EXTRATO ==============\n")
    print("Não foram realizadas transações.\n") if not extrato else extrato
    print(f"Saldo atual: R$ {saldo:.2f}\n")
    print("====================================\n")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Usuário já cadastrado!")
        return
    
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário: dd/mm/aaaa ")
    endereco = input("Digite o endereço do usuário: ")
    
    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })
    
    print("===Usuário cadastrado com sucesso!===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(numero_conta, agencia, usuarios):
    cpf = input ("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n===Conta criada com sucesso!===")
        return {
            "numero_conta": numero_conta,
            "agencia": agencia,
            "usuario": usuario
        }
        
    print("\n===Usuário não encontrado!===") 
    return None   
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)    
        print(textwrap.dedent(linha))

def main():
    
    saldo = 0
    limite = 2000
    extrato = ""
    numero_saques = 0
    usuarios = []    
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
            print(f"Depósito de R$ {valor} realizado com sucesso!")
            
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, AGENCIA, usuarios)
            
            if conta:
                contas.append(conta)
                print(f"Conta {numero_conta} criada com sucesso!")
                
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            print("Saindo...")
            break    
        
        else:
            print("Opção inválida! Selecione novamente a opção desejada.")        
      
main()        
