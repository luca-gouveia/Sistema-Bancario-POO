class Conta():
    def __init__(self,cliente,numero_conta,saldo,limite):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.limite = limite      #LIMITE NEGATIVO POSSIVEL

    def sacar(self, valor):
        if(self.saldo+self.limite < valor):
            print("***ERRO: Não é possivel SACAR esse valor!***")
        else:
            self.saldo -= valor
            print("\n***ALERTA: Foi SACADO R${} da sua conta!***".format(valor),
                  "\n--- Saldo: R${:.2f}".format(self.saldo))

    def depositar(self,valor):
        if(valor <= 0):
            print("***ERRO: Não é possivel DEPOSITAR esse valor!***")
        else:
            self.saldo += valor
            print("\n***ALERTA: Foi DEPOSITADO R${} na sua conta!***".format(valor),
                  "\n--- Saldo: R${:.2f}".format(self.saldo))




