agenda = []

while True:
    print('--------------------------------------------------------')
    print('                   AGENDA TELEFÔNICA                    ')
    print('--------------------------------------------------------')
    print('[1] - Ver contatos')
    print('[2] - Adicionar contatos')
    print('[3] - Sair')
    print()

    resposta = input(': ')

    match resposta:
        case 1:
            for agenda in agenda:
                print(agenda)

        case 2:
            nome = input('Digite o nome do contato: ')
            numero = input('Digite o número do contato: ')


    break

