idade = int(input("digite sua idade: "))
anosTra = int(input(" digite seus anos trabalhados: "))
if idade >= 60 and anosTra >= 25:
    print("Pode se aposentar !!!")
elif idade >= 65:
    print("Pode se aposentar !!!")
elif anosTra >= 30:
     print("Pode se aposentar !!!")
else:
    print(" Você não pode se aposentar!")
