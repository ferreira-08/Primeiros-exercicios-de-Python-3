soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o valor {} : '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} valores PARES e a soma foi {} '.format(cont, soma))
