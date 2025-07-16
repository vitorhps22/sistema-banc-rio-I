#desafio é criar um sistema bancário simples
#onde o usuário pode  depositar, sacar e extrato.

print("""
Bem-vindo ao Sistema Bancário Simples!
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair""")

saldo = 0
limite = 500
saques = 0
LIMITE_SAQUES = 3
extrato = []

while True:
    escolha = input("Escolha uma opção (1-4): ")
    if escolha == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif escolha == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > saldo:
            print("Saldo insuficiente para saque.")
        elif valor > limite:
            print(f"Valor acima do limite de saque de R$ {limite:.2f}.")
        elif saques >= LIMITE_SAQUES:
            print(f"Limite de saques atingido ({LIMITE_SAQUES} saques).")
        else:
            saldo -= valor
            saques += 1
            extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif escolha == "3":
        print("\nExtrato:")
        if extrato:
            for operacao in extrato:
                print(operacao)
        else:
            print("Nenhuma movimentação realizada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")


    elif escolha == "4":
        print("Saindo do sistema. Até logo!")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1-4).")
