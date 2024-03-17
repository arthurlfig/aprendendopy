#vou tenatr fazer uma calculadora simples
primeiroNumero = int(input("digite o primeiro numero da operação"))
operação = input(" qual tipo de operação vc dejesa realizar ? aperte 1- soma 2- subitração 3- multplicação 4-divisão 5 - para sair ")
segundoNumero = int(input("digite o segundo numero da operação"))
if operação == "1":
    print({primeiroNumero} + {segundoNumero})
elif operação == "2":
     print({primeiroNumero} * {segundoNumero})
elif operação == "3":
      print(f"{primeiroNumero} * {segundoNumero}")