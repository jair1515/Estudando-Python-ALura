def exibir_nome_do_programa():
    print('🆂🅰🅱🅾🆁 🅴🆇🅿🆁🅴🆂🆂\n')
    '''Essa função foi definida como o nome principal do nosso app'''

def exibir_opcoes():
    '''Está função foi criada para mostrar ao usuario as opções que ele devem seguir.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Função finalizar app como o nome mesmo diz foi criada para cada momento que for finalizar o app'''
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    '''Função criada quando o usuario escolhe uma opção que não existe ou invalida para aquele momento'''
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função garante que o titulo de cada opção permanessa na opção escolhida pelo usuario'''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função e responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurantes
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
def main():
    '''Já a função main e para retornar ao menu.'''        