@saldo.setter()
def saldo(self, saldo):
    if(self.saldo < 0):
        print("saldo inválido")
    else:
        self._saldo = saldo
        