from time import sleep

def gerenciar_contatos():
    contatos = {}

    while True:
        print('\n--- AGENDA DE CONTATOS ---')
        print('1. ADICIONAR CONTATOS')
        print('2. REMOVER CONTATOS')
        print('3. BUSCAR CONTATOS')
        print('4. EXIBIR TODOS OS CONTATOS')
        print('5. SAIR')

        opcao = input('ECOLHA UMA OPÇÃO:')

        if opcao == '1':
            nome = input('nome:')
            telefone = input('telefone:')
            email = input('email:')
            contatos[nome] = {'telefone': telefone, 'email': email}
            print(f"contato '{nome}' adicionado!")
        elif opcao == '2':
            nome = input('nome do contato para remover:')
            if nome in contatos:
                del contatos[nome]
                print(f'contato {nome}, removido!')
            else:
                print(f'contato {nome}, nao encontrado')
        elif opcao == '3':
            nome = input('nome do contato a buscar:')
            if nome in contatos:
                print(f'telefone: {contatos[nome]['telefone']}, email: {contatos[nome]['email']}')
            else:
                print(f'contato {nome}, nao encontrado')
        elif opcao == '4':
            for nome, info in contatos.items():
                print(f'nome: {nome}, telefone: {info['telefone']}, email: {info['email']}')
        elif opcao == '5':
            print('saindo...')
            sleep(1)
            print('...')
            sleep(1)
            print('...')
            sleep(1)
            break
        else:
            print('opcao invalida, tente novamente')


gerenciar_contatos()


