def menu():
    opcao = """
    Selecione a opção desejada:
    [1] Saque
    [2] Depósito
    [3] Extrato
    [4] Criar novo usuário
    [5] Listar contas
    [6] Criar nova conta
    [0] Sair
    """
    return int(input(opcao))

def saque(*, valor, extrato, saldo, num_saques, limite_valor, lim_saques):
    if num_saques < lim_saques:
        if float(valor) <= float(saldo):
            if valor > 0 and valor <= limite_valor:
                print("saque realizado!")
                saldo -= valor
                extrato += f"\n       -R${valor:.2f}"
                num_saques += 1
            else:
                print("Valor fora do limite")
        else:
            print("Não há saldo suficiente para essa operação")
    else:
        print("Limite de saques atingido")

    return extrato, saldo, num_saques

def deposito(valor, saldo, extrato,/):
    if valor > 0:
        print("Depósito realizado!")
        extrato += f"\n       +R${valor:.2f}"
        saldo += valor
    else:
        print("O valor do depósito deve ser maior que 0.")

    return saldo, extrato

def tirar_extrato(saldo,/,*, extrato):
    print("EXTRATO".center(30,"="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("=" * 30)
        
def criar_usuario(cpf, usuarios):
    for i in range(len(usuarios)):
        if cpf in usuarios[i]["cpf"]:
            print("Usuário já existente")
            return
    
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário: ")
    endereco = input("Digite o endereço do usuário: ")
    usuarios.append({"cpf":cpf,"nome":nome, "data_nascimento": data_nascimento, "endereço": endereco})
    print("Usuário criado!")

def criar_conta(cpf, usuarios, contas, n_agencia, n_conta):
    for i in range(len(usuarios)):
        if not cpf in usuarios[i]["cpf"]:
            print("Usuário não existente")
            return contas, n_conta
        else:
            usuario = usuarios[i]["nome"]
            
    agencia = n_agencia
    n_conta += 1
    contas.append({"agencia": agencia,"n_conta":n_conta, "usuario": usuario, "cpf": cpf})
    print("Conta criada!")
    return contas, n_conta

def listar_contas(contas):
    for conta in contas:
        print(conta)
        agencia = conta["agencia"]
        n_conta = conta["n_conta"]
        usuario = conta["usuario"]

        print(f"""
        Agência: {agencia}
        Nº da conta: {n_conta}
        Usuário: {usuario}""")

def main():    
    LIMITE_SAQUE_VALOR = 500
    LIMITE_SAQUE_QTD = 3
    N_AGENCIA = "0001"
    n_conta = 0
    num_saques = 0
    saldo = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1: #SAQUE
            valor = float(input("Escreva o valor do saque:  "))
            extrato, saldo, num_saques = saque(valor = valor, extrato = extrato, saldo = saldo, num_saques = num_saques, limite_valor = LIMITE_SAQUE_VALOR, lim_saques = LIMITE_SAQUE_QTD)

        elif opcao == 2:  #DEPÓSITO
            valor = float(input("Escreva o valor do depósito:  "))
            saldo, extrato = deposito(valor, saldo, extrato)

        elif opcao == 3:  #EXTRATO
            tirar_extrato(saldo, extrato = extrato)

        elif opcao == 4: #CRIAR USUÁRIO
            cpf = input("Digite seu cpf: ")
            cpf = "".join(n for n in cpf if n.isdigit())
            criar_usuario(cpf, usuarios)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6: #CRIAR CONTA
            cpf = input("Digite o cpf do usuário: ")
            cpf = "".join(n for n in cpf if n.isdigit())
            contas, n_conta = criar_conta(cpf, usuarios, contas, N_AGENCIA, n_conta)

        elif opcao == 0:
            print("Obrigado por utilizar nossos serviços bancários")
            break
        # else:
        #     print (opcao)
        #     print("Declare um valor especificado no menu")

main()