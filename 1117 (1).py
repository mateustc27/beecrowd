cont = 0
soma = 0
media = 0

while cont < 2:
    n = float(input())
    if n < 0 or n > 10.0:
        print("nota invalida")
    else:
        soma = soma + n
        cont = cont + 1
        media = soma / 2
    if cont == 2:
        break
print("media =", media)
