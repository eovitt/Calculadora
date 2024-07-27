def calculadora():

    print("Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"A soma é: {int(num1 + num2)}")

    elif escolha == 2:

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"A subtração é: {int(num1 - num2)}")

    elif escolha == 3:  

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"A multiplicação é: {int(num1 * num2)}")

    elif escolha == 4:

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if num2 != 0:
            print(f"A divisão é: {num1 / num2}")
    else:

        print("Opção inválida. Tente novamente.")
        print("Deseja continuar?")
        resposta = input("Sim/Não: ")

        if resposta.lower() == "sim":
            calculadora()
        else:
            print("Obrigado por usar a calculadora!")
            exit()
            
calculadora()




    