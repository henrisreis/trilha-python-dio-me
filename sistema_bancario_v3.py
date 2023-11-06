from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self): ...

    @abstractmethod
    def registrar(self, conta): ...


class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        detalhe_transacao = {
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        }
        self._transacoes.append(detalhe_transacao)
        

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_realizada = conta.depositar(self.valor)

        if transacao_realizada:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_realizada = conta.sacar(self.valor)

        if transacao_realizada:
            conta.historico.adicionar_transacao(self)


class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._agencia = "0001"
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico    

    def sacar(self, valor):
        saldo_atualizado = self.saldo - valor

        saque_impossibilitado = saldo_atualizado <= 0

        if saque_impossibilitado:
            print('Impossível realizar esse saque. O valor que se deseja sacar é superior ao saldo!')
            return False
        
        if valor <= 0:
            print('O valor informado é inválido!')
            return False

        self._saldo = saldo_atualizado
        print(f'SAQUE DE R${valor:.2f} REALIZADO COM SUCESSO!')
        
        return True

    def depositar(self, valor):
        if valor <= 0:
            print('O valor informado é inválido!')
            return False
        
        self._saldo += valor
        print(f'DEPÓSITO DE R${valor:.2f} REALIZADO COM SUCESSO!')
        
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = 0
        for transacao in self.historico.transacoes:
            if transacao["tipo"] == Saque.__name__:
                numero_saques += 1

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print('O valor a ser sacado excedeu o valor limite!')

        elif excedeu_saques:
            print('A quantidade limite de saques foi atingida!')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
        AGÊNCIA: {self.agencia}
        C/C: {self.numero}
        TITULAR: {self.cliente.nome}
        """    


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf    
