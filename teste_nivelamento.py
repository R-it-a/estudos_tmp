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



def reverte():
    """
    entrada: uma string
    saída: string ao contrário
    """
    return


def soma():
    """
    entradas:
        num_a : int, float
        num_b : int, float
    saida:
        resultado : int, float
    """
    return


def calculadora():
    """
    entradas:
        operacao : string
            descritor da operação. valores aceitos são "soma", "subtracao",
            "multiplicacao", "divisao", "potencia"
        num_a   : int, float
        num_b   : int, float

    saida:
        resultado : int, float

    requisitos:
        * cada operação deve ter sua própria função
        * se num_a ou num_b não forem do tipo correto, lance uma exceção
    """
    return


def printa_dicionario():
    """
    printa as chaves e valores de um dicionário no seguinte formato:
        {chave}\t{valor}
    entrada:
        dicionario
    saida: nulo
    """
    return


def printa_chaves_especificas():
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
    return


def ano_bissexto():
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
    return


def lista_maluca_inicio_0():
    """
    entradas:
        x, y : int
    saida:
        lista com todos os pares possíveis [x,y]

    exemplo:
        entrada: x = 2, y = 2
        saída: [[0,0],[0,1],[1,0],[1,1]]
    """
    return


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

    print_burro(0)
