import os




print('𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙚𝙨\n')




print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

op = int(input('Escolha uma opção: '))
#print("Você escolheu a opção {}".format (op))
#print(f"Você escolheu a opção {op}!")

def finalizar_app():
    os.system('clear')
    print('finalizando o app\n')






if op == 1:
    print('Cadastrar um restaurante')
elif op == 2:
    print('Listar restaurantes')
elif op == 3:
    print('Ativar restaurantes')
else:
    finalizar_app()    