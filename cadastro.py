#Apenas a tela de visualizaçao
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
    #se digitar 2, abre a tela de login
    elif (opcao == 2):
        print("===================")
        print("===tela de login===")
        print("===================")
    #se digitar 3, sai da execução
    elif(opcao == 3):
        print("Voce está saindo do cadastro, ate mais!")
        break
    #SE não for nem 1,2 ou 3, mostrar erro e repetir código
    else:
        print("Valor digitado , ivalido, use apenas números inteiros do menu")