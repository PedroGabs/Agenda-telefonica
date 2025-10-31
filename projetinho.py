import os
import time

agenda = []

def adicionar_contato(nome,numero):
    pessoa = {"nome" : nome, "numero" : numero}
    agenda.append(pessoa)

def editarContato():
    if not agenda:
        print("╔════════════════════════════════════════════════════╗")
        print("║ Nenhum contato salvo para editar.                  ║")
        print("╚════════════════════════════════════════════════════╝")
        time.sleep(1.7)
        os.system('cls')
        return

    os.system('cls')
    print("╔════════════════════════════════════════════════════╗")
    print("║ Qual contato você deseja editar?                   ║")
    print("╚════════════════════════════════════════════════════╝\n")
    for i, contato in enumerate(agenda):
        print('╔════════════════════════════════════════════════════════════════════════════════╗')
        print(f"[{i + 1}] - Nome: {contato['nome']} | Número: {contato['numero']}")
        print('╚════════════════════════════════════════════════════════════════════════════════╝\n')

    try:
        indice = int(input('Digite o índice do contato para editar: ')) - 1
        contato = agenda[indice]
    except (ValueError, IndexError):
        print('Índice inválido!')
        time.sleep(1.7)
        os.system('cls')
        return
    
    print('╔═════════════════════════╗')
    print('║O que você deseja editar?║')
    print('╠═════════════════════════╣')
    print('║[1] - Nome               ║')
    print('║[2] - Número             ║')
    print('║                         ║')
    print('╚═════════════════════════╝')
    escolha = int(input('R: '))

    match escolha:

        case 1:
            Novo_nome = input('Digite o nome modificado: ')
            if len(Novo_nome) >= 50:
                print("Nome muito grande! (limite de 50 caracteres)")

            else:
                print('nome modificado com sucesso!')
                contato['nome'] = Novo_nome
                time.sleep(2.2)
                os.system('cls')

        case 2:
            while True:
                try:
                    Novo_numero = input('Digite o número modificado: ')
                    if Novo_numero.isdigit() and len(Novo_numero) == 11:
                        print('Número modificado com sucesso!\n')
                        Novo_numero = int(Novo_numero)
                        contato['numero'] = Novo_numero
                        time.sleep(1.7)
                        os.system('cls')
                        break
                    else:
                        print("\nO número deve ter 11 dígitos!\n")
                        time.sleep(1.7)
                        os.system('cls')
                        break
                    
                except ValueError:
                    print('Digite apenas números!\n')
                    time.sleep(1.7)
                    os.system('cls')
            
        case _:
            print('Opção inválida\n')
            time.sleep(1.7)
            os.system('cls')

    
def filtrarContato(agenda, termo):
    resultados = []
    for contato in agenda:
        if termo.lower() in contato["nome"].lower():
            resultados.append(contato)
    return resultados

def Filtragem():
    os.system('cls')
    print("╔════════════════════════════════════════════════════╗")
    print("║ Qual contato você deseja procurar?                 ║")
    print("╚════════════════════════════════════════════════════╝")
    contato_procurado = input(':')
    os.system('cls')

    resultado = filtrarContato(agenda, contato_procurado)
    if resultado:
        for contato in resultado:
            print("╔════════════════════════════════════════════════════╗")
            print(f"Nome: {contato['nome']}                         ")
            print(f"Número: {contato['numero']}                     ")
            print("╚════════════════════════════════════════════════════╝\n")

        input('Pressione "ENTER" para voltar ao menu...')
        os.system('cls')
    else:
        print("╔══════════════════════════════════════════════════════════╗")
        print(f"Nenhum contato chamado {contato_procurado} foi encontrado!")
        print("╚══════════════════════════════════════════════════════════╝")
        time.sleep(2.2)
        os.system('cls')

def cadastroContato():
    nome = input('\nDigite o nome do contato: ')
    if len(nome) >= 50:
        print("Nome muito grande! (limite de 50 caracteres)")
        time.sleep(1.7)
        os.system('cls')
    else:
        while True:
            try:
                numero = input('Digite o número do contato com o DDD: ')
                if numero.isdigit() and len(numero) == 11:
                    print('Número cadastrado!\n')
                    numero = int(numero)
                    adicionar_contato(nome, numero)
                    time.sleep(1.7)
                    os.system('cls')
                else:
                    print("\nO número deve ter 11 dígitos!\n")
                    time.sleep(1.7)
                    os.system('cls')
                break
            except ValueError:
                print('Digite apenas números!\n')
                time.sleep(1.7)
                os.system('cls')

def RemoverContato():
    os.system('cls')
    print("╔════════════════════════════════════════════════════╗")
    print("║ Qual contato você deseja remover?                  ║")
    print("╚════════════════════════════════════════════════════╝")
    for i, contato in enumerate(agenda):
        print('╔════════════════════════════════════════════════════════════════════════════════╗')
        print(f"[{i + 1}] - Nome: {contato['nome']} | Número: {contato['numero']}")
        print('╚════════════════════════════════════════════════════════════════════════════════╝\n')

    try:
        indice = int(input('Digite o índice do contato para remover: ')) - 1
        contato = agenda.pop(indice)
        os.system('cls')
        print("╔═══════════════════════════════╗")
        print("║ Contato removido com sucesso! ║")
        print("╚═══════════════════════════════╝")
        time.sleep(2.2)
        os.system('cls')

    except (ValueError, IndexError):
        print('Índice inválido!')
        time.sleep(1.7)
        os.system('cls')

    

def visualizarContatos():
    if not agenda:
        os.system('cls')
        print("╔════════════════════════════════════════════════════╗")
        print("║ Nenhum contato salvo.                              ║")
        print("╚════════════════════════════════════════════════════╝")
        time.sleep(1.7)
        os.system('cls')
    else:
        os.system('cls')
        print("\nContatos salvos:")
        for contato in agenda:
            print('╔════════════════════════════════════════════════════════════════════════════════╗')
            print(f"Nome: {contato['nome']} | Número: {contato['numero']}")
            print('╚════════════════════════════════════════════════════════════════════════════════╝\n')
        input('Pressione "ENTER" para voltar ao menu...')
    os.system('cls')

#######################################     MENU     ########################################

print('Seja bem vindo a sua agenda telefônica!!\n')

while True:
    print('╔═══════════════════════════════════════════════════════════════════════════════════════════════╗')
    print('║ Agenda Telefônica. V1.0.4                                                                     ║')
    print('║ Autor: Pedro G.                                                                               ║')
    print('║ Descrição: Aplicativo de terminal para gerenciar contatos telefônicos.                        ║')
    print('║ Linguagem: Python 3                                                                           ║')
    print('╚═══════════════════════════════════════════════════════════════════════════════════════════════╝\n')
    print('╔══════════════════════════════════════════════════════╦════════════════════════════════════════╗')
    print('║                  AGENDA TELEFÔNICA                   ║                                        ║')
    print('╠══════════════════════════════════════════════════════╬════════════════════════════════════════╣')
    print(r'║                                                      ║                                        ║')
    print(r'║[1] - Ver contatos                                    ║             ______________             ║')
    print(r'║[2] - Adicionar contato                               ║            /   ,,____,,   \:.          ║')
    print(r'║[3] - Pesquisar contatos                              ║            |__| [][][] |__|:  :        ║')
    print(r'║[4] - Editar contatos                                 ║              /  [][][]  \   :  :       ║')
    print(r'║[5] - Remover contato                                 ║            /    [][][]    \   ..       ║')
    print(r'║[6] - Sair                                            ║             /   [][][]   \   :  :      ║')
    print(r'║                                                      ║           |________________|           ║')
    print(r'║                                                      ║                                        ║')
    print('╚══════════════════════════════════════════════════════╩════════════════════════════════════════╝')
    
    try: 
        resposta = int(input('R: '))
    except ValueError:
        print('\nUtilize apenas números!\n')
        time.sleep(1.7)
        os.system('cls')
        continue

    match resposta:
        case 1:
            visualizarContatos()

        case 2:
            cadastroContato()

        case 3:
            Filtragem()

        case 4:
            editarContato()

        case 5:
            RemoverContato()

        case 6:
            break

        case _:
            print("\nOpção inválida, tente novamente!\n")
            time.sleep(1.7)
            os.system('cls')
