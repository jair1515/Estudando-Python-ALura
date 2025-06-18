import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Intaliana', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Intaliano', 'ativo':False}]


def exibir_nome_do_programa():
    print('🆂🅰🅱🅾🆁 🅴🆇🅿🆁🅴🆂🆂\n')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante} já cadastrado: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 
    'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante ['categoria']
        ativo = restaurante ['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        op = int(input('Escolha uma opção: '))
        #print("Você escolheu a opção {}".format (op))
        #print(f"Você escolheu a opção {op}!")

        if op == 1:
            cadastrar_novo_restaurante()
        elif op == 2:
            listar_restaurantes()
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