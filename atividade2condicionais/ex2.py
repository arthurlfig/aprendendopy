a= float(input("digite um numero, o qual não pode ser 0: "))
b = float(input("digite um numero: "))
c = float(input("digite um numero: "))
resolução = (b ** 2) - 4 * a * c 
if resolução == 0:
    print("existem duas raízes reais iguais")
elif resolução > 0:
    print("existem duas raízes reais distintas")
else:
    print("existem duas raízes imaginárias conjugadas")