print('\n' * 2)

idade = int(input('Qual sua Idade?:'))

print('\n')

if idade > 0 and idade <= 12:
    print('Criança\n')
elif idade > 13 and idade <= 18:
    print('Adolescente\n')
else:
    print('Adulto\n')