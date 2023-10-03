menu = """
SISTEMA BANCÁRIO

Digite a operação:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

-> """

saldo = 0
extrato = ""
limite_valor = 500
limite_saques = 3
numero_saques = 0

while True:

    opcao = input(menu)
    print()

    if opcao not in 'dseq':
        print('Opção inválida!')
        continue

    if opcao == 'd':
        print('DEPÓSITO')
        deposito = float(input('Valor a depositar: '))
        
        deposito_invalido = deposito <= 0

        if deposito_invalido:
            print('Valor inválido!')

        else:
            print(f'Depósito de R${deposito:.2f} realizado com sucesso!')
            saldo += deposito
            extrato += f'\n| 1 DEPÓSITO DE R${deposito:.2f} | SALDO: R${saldo:.2f} |'
    
    if opcao == 's':

        excedeu_saques = numero_saques > limite_saques
        
        if excedeu_saques:
            print('Quantidade limite de saques atingida!')
            continue
        
        if saldo == 0:
            print('A conta não possui saldo!')
            continue

        print('SAQUE')
        saque = float(input('Valor a sacar: '))

        excedeu_limite = saque > limite_valor
        excedeu_saldo = saque > saldo
        saque_invalido = saque <= 0

        if excedeu_limite:
            print('Valor superior ao limite de R$500.00!')

        elif saque_invalido:
            print('Valor inválido!')

        elif excedeu_saldo:
            print('Impossível sacar! Valor superior ao saldo da conta!')

        else:
            print(f'Saque de R${saque:.2f} realizado com sucesso!')
            numero_saques += 1
            saldo -= saque
            extrato += f'\n| 1 SAQUE DE R${saque:.2f} | SALDO: R${saldo:.2f} |'


    if opcao == 'e':
        print('EXTRATO')
        print(extrato)

    if opcao == 'q':
        break