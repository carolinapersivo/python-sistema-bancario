menu = """
Selecione a opção desejada:
[1] Saque
[2] Depósito
[3] Extrato
[0] Sair
"""
LIMITE_SAQUE_VALOR = 500
LIMITE_SAQUE_QTD = 3
contador_saque = 0
saldo = 0
movimentacoes = 0
extrato = """
======= EXTRATO =======
"""

while True:
    opcao = int(input(menu))

    if opcao == 1:
        if contador_saque < 3:
            valor = float(input("Digite o valor do saque: R$"))
            if valor <= saldo:
                if valor > 0 and valor <= 500:
                    print("saque realizado!")
                    extrato += f"\n-R${valor:.2f}"
                    saldo -= valor
                    movimentacoes += 1
                    contador_saque += 1
                else:
                    print("Valor fora do limite")
            else:
                print("Não há saldo suficiente para essa operação")
        else:
            print("Limite de saques atingido")
    
    if opcao == 2:
        valor = int(input("Digite o valor do depósito: R$"))
        if valor > 0:
            print("Depósito realizado!")
            extrato += f"\n+R${valor:.2f}"
            saldo += valor
            movimentacoes += 1
        else:
            print("O valor do depósito deve ser maior que 0.")
    
    if opcao == 3:
        if not movimentacoes == 0:
            extrato += f"\n\nSALDO: R${saldo:.2f}"
            print(extrato)
        else:
            extrato += "\nNão foram realizadas movimentações."
            print(extrato.center(23))
    
    if opcao == 0:
        print("Obrigado porlizar nossos serviços bancários")
        break

