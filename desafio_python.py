def main():
    saldo = 0
    extrato = []
    saques_realizados = 0
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500

    menu = """
========== MENU ==========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

    while True:
        opcao = input(menu).strip()

        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: "))
                
                if valor > 0:
                    saldo += valor
                    extrato.append(f"Depósito: R$ {valor:.2f}")
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado é inválido.")
            except ValueError:
                print("Operação falhou! Valor inválido informado.")

        elif opcao == "2":
            if saques_realizados >= LIMITE_SAQUES:
                print("Operação falhou! Limite diário de saques atingido.")
                continue

            try:
                valor = float(input("Informe o valor do saque: "))

                if valor > LIMITE_POR_SAQUE:
                    print(f"Operação falhou! O valor máximo por saque é R$ {LIMITE_POR_SAQUE:.2f}.")
                elif valor > saldo:
                    print("Operação falhou! Saldo insuficiente.")
                elif valor > 0:
                    saldo -= valor
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    saques_realizados += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado é inválido.")
            except ValueError:
                print("Operação falhou! Valor inválido informado.")

        elif opcao == "3":
            print("\n========== EXTRATO ==========")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for movimentacao in extrato:
                    print(movimentacao)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("============================")

        elif opcao == "4":
            print("Obrigado por utilizar nosso sistema bancário!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()