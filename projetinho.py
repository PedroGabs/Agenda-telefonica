import os
import time

agenda = []

def adicionar_contato(nome,numero):
    pessoa = {"nome" : nome, "numero" : numero}
    agenda.append(pessoa)

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

def visualizarContatos():
    if not agenda:
        print("╔════════════════════════════════════════════════════╗ ")
        print("║ Nenhum contato salvo.                              ║ ")
        print("╚════════════════════════════════════════════════════╝")
        time.sleep(1.7)
        os.system('cls')
    else:
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
    print('╔══════════════════════════════════════════════════════╦════════════════════════════════════════╗')
    print('║                  AGENDA TELEFÔNICA                   ║                                        ║')
    print('╠══════════════════════════════════════════════════════╬════════════════════════════════════════╣')
    print(r'║                                                      ║                                        ║')
    print(r'║[1] - Ver contatos                                    ║             ______________             ║')
    print(r'║[2] - Adicionar contatos                              ║            /   ,,____,,   \:.          ║')
    print(r'║[3] - Sair                                            ║            |__| [][][] |__|:  :        ║')
    print(r'║                                                      ║              /  [][][]  \   :  :       ║')
    print(r'║                                                      ║             /   [][][]   \   :  :      ║')
    print(r'║                                                      ║            /    [][][]    \   ..       ║')
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
            break

        case _:
            print("\nOpção inválida, tente novamente!\n")
            time.sleep(1.7)
            os.system('cls')
