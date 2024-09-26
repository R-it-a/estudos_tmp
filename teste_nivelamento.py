from itertools import combinations

""" NIVELAMENTO PYTHON """
def concatena(a, b):
    """
    entrada: duas strings
    saída: strings concatenadas
    """
    c = a + b

    return c


def print_burro(a):
    """
    entrada: um int

    se a entrada for ímpar, printe "estranho"
    se a entrada for par e estiver no intervalo [2,5] (inclusivo), printe "não é estranho"
    se a entrada for par e estiver no intervalo [6,20] (inclusivo) printe "estranho"
    se a entrada for par e maior que 20, printe "não é estranho"
    """
    assert a > 0, "variavel negativa OU 0"
    if a%2 != 0:
        print("strangethings")
    elif a%2 == 0 and 2 <= a <= 5:
        print("notstrange")
    elif a%2 == 0 and 6 <= a <= 20:
        print("estranho")
    else:
        print("não é estranho")
    return


def concatena_n(entrada):
    """
    entrada: uma lista com n strings (variável)
    saída: strings concatenadas
    """
    assert type(entrada) == list
    concatenada = ''
    for palavra in entrada:
        #concatenada = concatenada + palavra
        concatenada = concatena(concatenada, palavra)
    return concatenada



def reverte(a):
    """
    entrada: uma string
    saída: string ao contrário
    """
    b = a [::-1]

    return b


def soma(a, b):
    """
    entradas:
        num_a : int, float
        num_b : int, float
    saida:
        resultado : int, float
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        c = a + b
        return c

#class Calculadora:
#   """
#   entradas:
#       operacao : string
#           descritor da operação. valores aceitos são "soma", "subtracao",
#           "multiplicacao", "divisao", "potencia"
#       num_a   : int, float
#       num_b   : int, float

#   saida:
#       resultado : int, float

#   requisitos:
#       * cada operação deve ter sua própria função
#       * se num_a ou num_b não forem do tipo correto, lance uma exceção
#   """

#   def add(x, y):
#       return x + y

#   def subtract(x, y):
#       return x - y

#   def multiply(x, y):
#       return x * y

#   def divide(x, y):
#       return x / y

#   print("Select operation.")
#   print("1.Add")
#   print("2.Subtract")
#   print("3.Multiply")
#   print("4.Divide")

#   while True:

#       choice = input("Enter choice(1/2/3/4): ")


#       if choice in ('1', '2', '3', '4'):
#           try:
#               num1 = float(input("Enter first number: "))
#               num2 = float(input("Enter second number: "))
#           except ValueError:
#               print("Invalid input. Please enter a number.")
#               continue

#           if choice == '1':
#               print(num1, "+", num2, "=", add(num1, num2))

#           elif choice == '2':
#               print(num1, "-", num2, "=", subtract(num1, num2))

#           elif choice == '3':
#               print(num1, "*", num2, "=", multiply(num1, num2))

#           elif choice == '4':
#               print(num1, "/", num2, "=", divide(num1, num2))


#           next_calculation = input("Let's do next calculation? (yes/no): ")
#           if next_calculation == "no":
#               break
#       else:
#           print("Invalid Input")


def printa_dicionario(input_dict):
    """
    printa as chaves e valores de um dicionário no seguinte formato:
        {chave}\t{valor}
    entrada:
        dicionario
    saida: nulo
    """
    for key, value in input_dict.items():
        print(f"{key}:\t{value}")

    return

def printa_chaves_especificas(input_dict):
    """
    printa as chaves e valores de um dicionário no seguinte formato:
        {chave}\t{valor}
    SE elas estiverem dentro da lista de chaves possíveis
    entrada:
        dicionario : dict
        chaves_permitidas : lista
    saida: nulo

    requisitos
        * se uma chave da lista não existir no dicionário, printe o erro dizendo
        "chave {chave} não existe", mas não interrompa a execução
    """
    for key, value in input_dict.items():
        if key in ['Rita', 'Giovana', 'Jaqueline', 'Sofia']:
            print(f"{key}:\t{value}")
        else:
            print(f"Chave {key} não existe")
            continue

    return


def ano_bissexto(ano):
    """
    roubei do hackerrank:

    An extra day is added to the calendar almost every four years as February
    29, and the day is called a leap day. It corrects the calendar for the fact
    that our planet takes approximately 365.25 days to orbit the sun. A leap
    year contains a leap day.

    In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless: The year can be
    evenly divided by 100, it is NOT a leap year, unless: The year is also
    evenly divisible by 400. Then it is a leap year.

    This means that in the Gregorian calendar, the years 2000 and 2400 are leap
    years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

    entrada:
        ano : int
            ano que vamos descobrir se é bissexto ou não
    saída:
        bissexto : booleano
            variável que dirá se o ano é bissext ou não
    """
    #ano = input("Qual o ano que vamos checar?")
    if (ano %4) == 0:

        if (ano %100) == 0:

            if (ano %400) == 0:
                print("It is a leap year")
            else:
                print("It is not a leap year")

    return ano


def lista_maluca_inicio_0(x, y):
    """
    entradas:
        x, y : int
    saida:
        lista com todos os pares possíveis [x,y]

    exemplo:
        entrada: x = 2, y = 2
        saída: [[0,0],[0,1],[1,0],[1,1]]
    """
    res = isinstance(x, int)
    re = isinstance(y, int)


   # assert type(x) == int
    #assert type(y) == int

    lista = []
    for num in range(x):

        lista.append(num)

    return lista


def lista_maluca_inicio_1():
    """
    entradas:
        x, y : int
    saida:
        lista com todos os pares possíveis [x,y]

    exemplo:
        entrada: x = 2, y = 2
        saída: [[1,1],[1,2],[2,1],[2,2]]
    """
    return
#UM COMEÇA NO 0 OUTRO NO 1

if __name__ == "__main__":
    #saida = concatena("rita", "tiago")
    #assert saida == "ritatiago" #ter certeza q vai sair o q quero, mais rapido pra checar
    #saida = concatena_n(["rita", "tiago", "sofia", "giovana"])
    #print("retorno final de jedi", saida)
    #assert saida == "ritatiago" #ter certeza q vai sair o q quero, mais rapido pra checar

    #print_burro(0)
    #print(reverte("rita"))
    #print(soma(3, 3))
    #c = soma(1, 3)
    #print(c)
    #c = soma(1,3)
    #print(c)
    #input_dict = {
      #  'Rita': '1',
     #   'Giovana': '2',
    #    'Tiago': '3'
   #}


    #printa_chaves_especificas(input_dict)
   #ano = ano_bissexto(2400)
    lista_maluca_inicio_0(3,2)
