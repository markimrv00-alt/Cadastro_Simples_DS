while True:
    print("==================")
    print("Sitema de Cadastro")
    print("==================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))
    #se o usuario digitar o valor 1, vai ser exibido
    # a ação abaixo:
    if (opcao == 1) :
        print("========================")
        print("====Tela de Cadastro====")
        print("========================")
    elif (opcao == 2):
        print("===================")
        print("===tela de login===")
        print("===================")
    else:
        print("Voce está saindo do cadastro, ate mais!")
        break