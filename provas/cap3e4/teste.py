def calculadora():
    n1 = int(input("Insira o primeiro número:"))
    n2 = int(input("Insira o segundo número:"))
    operador = input("Insira o operador (+, -, %, x): ")


    if operador == "%":
        print(n1 / n2)
    elif operador == "x":
        print(n1 * n2)
    elif operador == "+":
        print(n1 + n2)
    elif operador == "-":
        print(n1 - n2)


calculadora()