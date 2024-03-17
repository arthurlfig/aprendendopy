sexoDaPessoa = input("insira o seu sexo : ")
H = float(input("insira sua altura : "))
PesoM = (72.7* H) - 58
pesoF = (62.1* H) - 44.7
if sexoDaPessoa == "masculino":
    print(f"seu peso ideal é {PesoM}")
elif sexoDaPessoa == "feminino":
    print(f"seu peso ideal é {pesoF}")
