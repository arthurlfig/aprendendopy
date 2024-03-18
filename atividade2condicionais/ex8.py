idade = int(input("digite sua idade para ver se você é eleitor ou não: "))
if idade < 16:
    print("vc nao é eleitor")
elif idade > 16 and idade < 18:
    print("Eleitor facultativo")
elif idade > 65:
    print("Eleitor facultativo")
else:
    print("Eleitor obrigatorio")