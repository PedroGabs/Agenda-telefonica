agenda = []

def adicionar_contato(nome,numero):
        pessoa = {"nome" : nome, "numero" : numero}
        agenda.append(pessoa)


while True:
    print('--------------------------------------------------------')
    print('                   AGENDA TELEFÔNICA                    ')
    print('--------------------------------------------------------')
    print('[1] - Ver contatos')
    print('[2] - Adicionar contatos')
    print('[4] - Sair')
    print()

    resposta = input('R: ')

    print()

    match resposta:
        case '1':
            if not agenda:
                print("📭 Nenhum contato salvo.")
            else:
                print("📒 Contatos salvos:")
            for contato in agenda:
                print('--------------------------------------------------------')
                print(f"Nome: {contato['nome']} | Número: {contato['numero']}")
                print('--------------------------------------------------------')

        case '2':
            nome = input('Digite o nome do contato: ')
            while True:
                try:
                    numero = int(input('Digite o número do contato: '))
                    break
                except ValueError:
                    print('⚠ Digite apenas números!')

            adicionar_contato(nome, numero)

        case '3':
            break

