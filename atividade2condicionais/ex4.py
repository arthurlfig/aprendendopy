n1 = float(int(" digite sua primeira nota"))
n2 = float(int(" digite sua segunda nota"))
n3 = float(int(" digite sua  terceira nota 1"))
n4 = float(int(" digite sua quarta nota "))
media = (n1 + n2 + n3 + n4 ) / 4 
if media >= 7:
    print(f"vc foi aprovado(a)")
elif media >= 4 and media <7:
    print(" vai de recuperação")
else:
    print("Reprovado!!")