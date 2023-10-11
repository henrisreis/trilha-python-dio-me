def exibir_extrato(*, extrato):
    print(extrato)


def criar_conta(conta_corrente, agencia, cpf):
    conta_corrente += 1
    conta = dict(conta=conta_corrente, agencia=agencia, cpf=cpf)
    lista_contas.append(conta)

    for cliente in lista_clientes:
        if cpf_cadastro == cliente['cpf']:
            cliente['conta'] = conta
            
    print('CONTA CORRENTE CADASTRADA COM SUCESSO!')

    return conta_corrente, lista_contas, lista_clientes


def criar_usuario(lista_clientes):
    nome = input('Nome: ')
    nascimento = input('Data de nascimento: ')
    endereco = input('Endereço [logradouro, nº - bairro - cidade/uf]: ')

    cliente = dict(nome=nome, nascimento=nascimento, cpf=cpf, endereco=endereco)
    lista_clientes.append(cliente)
    lista_cpfs = [cliente['cpf'] for cliente in lista_clientes]

    print('USUÁRIO CRIADO COM SUCESSO!')

    return lista_clientes, lista_cpfs


def sacar(*, saldo, valor, extrato, limite_valor, numero_saques):
    excedeu_limite = valor > limite_valor
    excedeu_saldo = valor > saldo
    saque_invalido = valor <= 0

    if excedeu_limite:
        print('Valor superior ao limite de R$500.00!')
        return

    if saque_invalido:
        print('Valor inválido!')
        return

    if excedeu_saldo:
        print('Impossível sacar! Valor superior ao saldo da conta!')
        return
    
    print(f'SAQUE DE R${valor:.2f} REALIZADO COM SUCESSO!')

    numero_saques += 1
    saldo -= valor
    extrato += f'\n| 1 SAQUE DE R${valor:.2f} | SALDO: R${saldo:.2f} |'

    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    saldo += valor
    extrato += f'\n| 1 DEPÓSITO DE R${valor:.2f} | SALDO: R${saldo:.2f} |'

    print(f'DEPÓSITO DE R${deposito:.2f} REALIZADO COM SUCESSO!')

    return saldo, extrato


menu = """
SISTEMA BANCÁRIO

Digite a operação:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Cadastrar cliente
[cc] Cadastrar conta-corrente

-> """


OPCOES = ['d', 's', 'e', 'q', 'c', 'cc']
AGENCIA = '001'
LIMITE_VALOR = 500
LIMITE_SAQUES = 3
extrato = ''
saldo = 0
conta_corrente = 0
numero_saques = 0
lista_clientes = []
lista_contas = []
lista_cpfs = []


while True:
    opcao = input(menu)
    print()


    if opcao not in OPCOES:
        print('Opção inválida!')
        continue


    if opcao == 'c':
        print('CADASTRO DE CLIENTE')
        cpf = input('CPF: ')

        if cpf in lista_cpfs:
            print('Cliente já cadastrado.')
            continue

        lista_clientes, lista_cpfs = criar_usuario(lista_clientes)


    if opcao == 'cc':
        print('CADASTRO DE CONTA CORRENTE')
        cpf_cadastro = input('CPF para cadastro de conta corrente: ')

        if cpf_cadastro not in lista_cpfs:
            print('O cliente precisa ser cadastrado!')
            continue
        
        conta_corrente, lista_contas, lista_clientes = criar_conta(conta_corrente, AGENCIA, cpf_cadastro)


    if opcao == 'd':
        print('DEPÓSITO')
        deposito = float(input('Valor a depositar: '))
        
        deposito_invalido = deposito <= 0

        if deposito_invalido:
            print('Valor inválido!')
            continue

        saldo, extrato = depositar(saldo, deposito, extrato)


    if opcao == 's':

        excedeu_saques = numero_saques > LIMITE_SAQUES
        
        if excedeu_saques:
            print('Quantidade limite de saques atingida!')
            continue
        
        if saldo == 0:
            print('A conta não possui saldo!')
            continue

        print('SAQUE')
        saque = float(input('Valor a sacar: '))

        saldo, extrato = sacar(saldo=saldo, valor=saque, extrato=extrato, limite_valor=LIMITE_VALOR, numero_saques=numero_saques)


    if opcao == 'e':
        print('EXTRATO')
        exibir_extrato(extrato=extrato)


    if opcao == 'q':
        break