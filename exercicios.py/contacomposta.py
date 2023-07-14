import datetime
from Extrato import Extrato


class Conta:

    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data abertura = datetime.datetime.today()
        self.extrato = Extrato()
        
    def depositar(self, valor):
        self.saldo += valorself.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today ()])
        
    def sacar(self, valor):
        if self.saldo < valor:
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True
        
    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            retun "Não existe saldo suficiente"
            
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return "Transferencia Realizada"
        
    def gerarsaldo(self):
        print(f"numero: {self.numero}\n saldo: {self.saldo}")
                
        
