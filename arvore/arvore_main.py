import arvore

if __name__ == '__main__':
    raiz: arvore.No = None
    while True:
        print('Selecione uma opção:')
        print('1 - Criar raiz')
        print('2 - INSERT')
        print('3 - DELETE')
        print('4 - SEARCH')
        print('5 - Exibir Pré-ordem')
        print('6 - Exibir Em-ordem')
        print('7 - Exibir Pós-ordem')
        print('8 - Sair')

        opcao = int(input('Opção: '))
        if opcao == 1:
            print("Digite o valor(numérico e inteiro) da raiz: ", end='')
            dado = int(input())
            raiz = arvore.No(dado)
        elif opcao == 2:
            print("Digite o valor(numérico e inteiro) a ser inserido: ", end='')
            dado = int(input())
            arvore.insert(raiz, dado)
        elif opcao == 3:
            print("Digite o valor(numérico e inteiro) a ser excluído: ", end='')
            dado = int(input())
            no = arvore.delete(raiz, dado)
            if no is None:
                print('Valor não encontrado')
            else:
                print('Valor excluído')
        elif opcao == 4:
            print("Digite o valor(numérico e inteiro) a ser pesquisado: ", end='')
            dado = int(input())
            no = arvore.search(raiz, dado)
            if no is None:
                print('Valor não encontrado')
            else:
                print('Valor encontrado')
        elif opcao == 5:
            print("Exibindo Pré-ordem")
            arvore.imprimir_pre_ordem(raiz)
        elif opcao == 6:
            print("Exibindo Em-ordem")
            arvore.imprimir_em_ordem(raiz)
        elif opcao == 7:
            print("Exibindo Pós-ordem")
            arvore.imprimir_pos_ordem(raiz)
        elif opcao == 8:
            break
        else:
            print('Opção desconhecida!')
