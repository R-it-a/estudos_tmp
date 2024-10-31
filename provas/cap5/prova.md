Prova 5: Condicionais e recursão

1. Qual a diferença entre as expressões `x == 1` e `x = 1`?
No primeiro caso, quando colocamos "x == 1", estamos comparando o valor de x à 1. Já no segundo caso, com um único "=", estamos atribuindo 1 à variável x, que agora terá esse valor.


2. Qual a saída do código abaixo? Justifique

```python
def concatena(lista_valores, verboso):
	str_concatenada = ""
	
	for item in lista_valores:
		str_concatenada += item + ", "
		if verboso = True:
			print(str_concatenada)
			
	return str_concatenada 

concatena(lista_valores=["a", "rita", "é", "estudiosa"], verboso=True)
```  
R: Essa função retorna um erro, porque está atribuindo True à variável verboso, o correto seria:
'''
def concatena(lista_valores, verboso):
	str_concatenada = ""
	
	for item in lista_valores:
		str_concatenada += item + ", "
		if verboso == True:
			print(str_concatenada)
			
	return str_concatenada 
'''
o que printaria:
a, 
a, rita, 
a, rita, é, 
a, rita, é, estudiosa, 

3. Qual a saída do código abaixo:
```python
def funcao_misteriosa(lista_valores):
	x = 0
	y = 0
	for item in lista_valores:
		if i % 2 != 0:
			x += 1
		else:
			y += 1
	return x, y
	
lista_valores = [0,1,2,3,4,5,6,7,8,9,10]
```
R: A função como está escrita não roda, porque ao escolher item para iterar, é preciso usar item no if também, e não i (if i % 2 != 0:). Quando isso é corrigido, a função retorna a soma dos impares e dos pares, 
usando o operandor módulo% para distinguir quem é ou não impar, e somando às variáveis x, y que funcionam como counters.


4. a) Remova os ifs internos:
```
if x > 0:
	if y < 10:
		print("x > 0, y < 10")
	elif y > 10:
		print("x > 0, y > 10")
elif x <= 0:
	if y < 10:
		print("x <= 0, y < 10")
	elif y > 10: 
		print("x <= 0, y > 10")
``` 

if x > 0 and y < 10:
    print("x > 0, y < 10")
elif y > 10:
    print("x > 0, y > 10")
elif x <= 0 and y < 10:
    print("x <= 0, y < 10")
elif y > 10:
    print("x <= 0, y > 10")



b) Existe algum caso que não é coberto pela condição acima?
Não.

5. Qual é o comando para se aceitar entradas do usuário? 
O compando "input"

6. Escreva uma função que receba uma palavra do usuário e, se a palavra tiver menos de 5 caracteres, duplica ela e então inverte ela. Caso contrário, apenas a inverte.
Exemplo de entrada: "oi"
Saída "ioio"

Exemplo de entrada: "giovana"
Saída: "anavoig"


def tranformar_palavra(palavra):
    if len(palavra) < 5:
        double = palavra * 2
        last_word = double[::-1]
    else:
        last_word = palavra * 2

    print(last_word)

7. O que é uma função recursiva? 
Funções recursivas são funções que são usadas/chamadas dentro do seu próprio corpo.


8. Qual a saída da função abaixo:
```python
def f(n):
    if n <= 0:
        print('caso base')
    else:
        print(n)
        f(n-1)

f(5)        
```
5
4
3
2
1
caso base

7. Dado `x = True` e `y = False`, qual a saída das condições abaixo:

a) x and y
False

b) x or y
True

c) not x and y
True

d) not x and not y
False

e) not x or not y
True


8. Exercício roubado do livro:
"If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a test to see if it is possible to form a triangle:

"If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)"

Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks with the given lengths. Hint: Use a chained conditional."

def is_triangle(x1, x2, x3):
    if x1 + x2 >= x3 and x1 + x3 >= x2 and x2 + x3 >= x1:
        print("Yes")
    else:
        print("No")


9. Usando condicionais, crie uma calculadora simples (sim, você não vai escapar dela). O usuário deverá fornecer dois número e um operador (+, -, *, /) e você retornará o resultado. 
Exemplo de entrada: 1, 2, +
Saída: 3

Exemplo de entrada: 2, 2, a
Saída: "Operador incorreto"

R:
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
