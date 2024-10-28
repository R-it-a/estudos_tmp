Prova 5: Condicionais e recursão

1. Qual a diferença entre as expressões `x == 1` e `x = 1`?

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

b) Existe algum caso que não é coberto pela condição acima?

5. Qual é o comando para se aceitar entradas do usuário? 

6. Escreva uma função que receba uma palavra do usuário e, se a palavra tiver menos de 5 caracteres, duplica ela e então inverte ela. Caso contrário, apenas a inverte.
Exemplo de entrada: "oi"
Saída "ioio"

Exemplo de entrada: "giovana"
Saída: "anavoig"

7. O que é uma função recursiva? 

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

7. Dado `x = True` e `y = False`, qual a saída das condições abaixo:

a) x and y
b) x or y
c) not x and y
d) not x and not y
e) not x or not y

8. Exercício roubado do livro:
"If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a test to see if it is possible to form a triangle:

"If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)"

Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks with the given lengths. Hint: Use a chained conditional."

9. Usando condicionais, crie uma calculadora simples (sim, você não vai escapar dela). O usuário deverá fornecer dois número e um operador (+, -, *, /) e você retornará o resultado. 
Exemplo de entrada: 1, 2, +
Saída: 3

Exemplo de entrada: 2, 2, a
Saída: "Operador incorreto"

