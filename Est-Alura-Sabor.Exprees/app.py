import os

restaurantes = []


def exibir_nome_do_programa():
    print('𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙚𝙨\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('clear')
    print('finalizando o app\n')


def opcao_invalida():
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()


def cadastrar_novo_restaurante():
    os.system('clear')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal') 
    main()


def escolher_opcoes():
    try:
        op = int(input('Escolha uma opção: '))
        #print("Você escolheu a opção {}".format (op))
        #print(f"Você escolheu a opção {op}!")

        if op == 1:
            cadastrar_novo_restaurante()
        elif op == 2:
            print('Listar restaurantes')
        elif op == 3:
            print('Ativar restaurantes')
        elif op == 4:
            finalizar_app() 
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')   
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()