Uni = input("Em qual universidade vc estuda?")
n1 = float(input(" digite sua primeira nota"))
n2 = float(input(" digite sua segunda nota"))
media = (n1 + n2) / 2
if Uni =="pucpr" and media >= 7:
    print("Aprovado!!!")
elif Uni == "pucpr" and media < 7 and media > 4:
    print("recuperação")
elif Uni == "pucpr" and media < 4:
    print("Reprovado")
elif Uni == "Unicamp" and media >= 5:
    print("Aprovado!!")
elif Uni == "Unicamp" and media < 5:
    print("recuperação")