num = int(input('Digite um número inteiro '))
print('''Escolha uma base para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Qual sua opção? '))
if opção == 1:
    print('{} convertido para binário fica {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal fica {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁVILDA ')