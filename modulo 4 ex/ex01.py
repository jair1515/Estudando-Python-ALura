import os

pessoas = [{'nome':'Jair', 'idade':'24', 'cidade':'Sarandi'}]

os.system('clear')
for pessoa in pessoas:
    Usuario = pessoa['nome']
    Anos = pessoa['idade']
    Local = pessoa['cidade']
print(f'Encontramos o {Usuario} com {Anos} anos, que mora na cidade de {Local}')

Usuario = input('\nDigite um novo nome: ')
print(f'voce atulizou seu nome para {Usuario}')




