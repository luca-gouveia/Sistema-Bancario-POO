'''
Author: Luca Gouveia
Created on 22/06/18
'''

from cliente import Cliente
from conta import Conta

nome = str(input("Nome do Titular: "))
cpf = str(input("CPF do Titular: "))
idade = int(input("Idade do Titular: "))
numero = str(input("Digite o Numero da Conta: "))
saldo = float(input("Digite o seu saldo inicial: "))

pessoa1 = Cliente(nome,cpf,idade)
conta1 = Conta(pessoa1,numero,saldo,100) # LIMITE DEFINIDO COMO 100

print("====================\n"+str(pessoa1),"\n"+"N°Conta:",conta1.numero_conta,"\n"+"Saldo: R${:.2f}".format(conta1.saldo),"\n====================")

resposta = ''
lista_resposta = ['DEPOSITAR','SACAR','CONSULTAR SALDO','SAIR']

while (resposta != 'SAIR'):
    resposta = str(input("\nVOCÊ QUER *DEPOSITAR, *SACAR, *CONSULTAR SALDO OU *SAIR? ")).upper()

    if(resposta == 'DEPOSITAR'):
        valor = float(input("\nDIGITE O VALOR DO DEPOSITO: "))
        conta1.depositar(valor)

    elif(resposta == 'SACAR'):
        valor = float(input("\nDIGITE O VALOR DO SAQUE: "))
        conta1.sacar(valor)

    elif(resposta == "CONSULTAR SALDO"):
        print("\n--- SEU SALDO É DE R${:.2f}".format(conta1.saldo))

    elif(resposta not in lista_resposta):
        print("\nTENTE NOVAMENTE. . .")

