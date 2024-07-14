# -*-coding: utf-8-*-

def calcula_segundos(horas, minutos, segundos):
    """
    dado o número de horas, minutos e segundos, calcule o total de segundos
    """
    minutos_trabalhados = horas * 60
    segundos_trabalhados = minutos_trabalhados * 60 + minutos * 60 + segundos

    return segundos_trabalhados


def preco_hora(horas, salario):
    """
    se você ganha um salario por mes, quanto vale sua hora de trabalho?
    """
    horas_trabalho = horas * 4
    salario_por_hora = salario / horas_trabalho

    return salario_por_hora


def preco_segundo(horas, salario):
    """
    se você ganha um salario por mes, quanto vale o seu segundo de trabalho?
    """
    horas_semanal = horas * 4
    segundos_trabalhados = calcula_segundos(horas=horas_semanal,minutos=0,segundos=0)
    print(segundos_trabalhados)
    segundos_por_hora = salario / segundos_trabalhados

    return segundos_por_hora



if __name__ == "__main__":
    # questao 1: quantos segundos existem em 42 minutos e 42 segundos?
    total_segundos = calcula_segundos(horas=0, minutos=42, segundos=42)
    print(f"em 42 minutos e 42 segundos existem {total_segundos} segundos")

    # questao 2: se você ganha 5 mil por mês, trabalhando 40 horas,
    # quanto vale sua hora?
    preco_hora_ritinha = preco_hora(horas=50, salario=6000)
    print(f"o preço da minha hora trabalhada foi {preco_hora_ritinha}")

    # questao 3: se você trabalha 40 horas por mês, quantos segundos você
    # trabalha? e quanto vale o seu segundo trabalhado?
    segundos_trabalhados = calcula_segundos(horas=50, minutos=0, segundos=0)
    preco_segundo_ritinha = preco_segundo(horas=50, salario=6000)
    print(f"o preço do meu segundo trabalhado é {segundos_trabalhados}")

    print(f"eu trabalhei 50 horas, o que significa que trabalhei {segundos_trabalhados} segundos")
    print(f"o preço do meu segundo trabalhado foi {preco_segundo_ritinha} reais")
