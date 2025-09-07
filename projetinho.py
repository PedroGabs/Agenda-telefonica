agenda = []

def adicionar_contato(nome,numero):
        pessoa = {
            "nome:" == nome, 
            "número" == numero
        }
        agenda.append(pessoa)


while True:
    print('--------------------------------------------------------')
    print('                   AGENDA TELEFÔNICA                    ')
    print('--------------------------------------------------------')
    print('[1] - Ver contatos')
    print('[2] - Adicionar contatos')
    print('[3] - Sair')
    print()

    resposta = input(': ')

    print()

    match resposta:
        case '1':
            for agenda in agenda:
                print('--------------------------------------------------------')
                print(agenda)
                print('--------------------------------------------------------')

        case '2':
            print()
            nome = input('Digite o nome do contato: ')
            print()
            numero = input('Digite o número do contato: ')
            print()

            adicionar_contato(nome, numero)

        case '3':
            break

