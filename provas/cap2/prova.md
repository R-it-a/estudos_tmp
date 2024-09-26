# Capítulo 2


## Teórico
1. Como você adiciona um comentário em um código Python? Como você adiciona um comentário que engloba múltiplas linhas? (0.5 pt)
Comentário de uma linha: #
Comentário de múltiplas linhas ''' '''

2. O que é um erro de sintaxe? O que é um erro de runtime? O que é um erro semântico? Dê um exemplo de cada. (1.5 pts)
Erro de sintaxe é quando a forma como seu código está escrito está errada, não está de acordo com a linguagem Python.
Erro de runtime é quando o código tem alguma exceção, algo que você programou está com sintaxe correta, mas não executa .
Erro semântico é quando o que vc escreveu, apesar de sintaticamente correto, não executa da forma como vc gostaria, o sentido do código está errado.

3. Como você importa um módulo? É possível importar uma função específica de um módulo em vez de ele todo? Se sim, como? (1 pt)
Com import, e é possível instanciar uma função sem importar o modulo inteiro, tornando a função pública, e não deixando ela privada.


4. O que é um argumento de uma função? (1 pt)
O argumento é o que colocamos entre parênteses no fim de uma função, e indica o que ela tem que receber para ser corretamente executada. Ex. def blablabla(argumento):
blablabla usa argumento dentro do código para executar algo.


5. Qual é a saída? (1 pt)
	a) print("número"); print(1/2)
	número
	0.5

	b) print("número", 1+1)
	número 2
	c) num = 6; print(f"número {num%3})
	número 2
	d) num = 4; print("numero {}".format(num + 3))
	numero 7

6. O que é um palavra reservada na linguagem (keyword)? Você consegue sobrescrever o seu valor? (1 pt)
São palavras que tem função especial na linguagem, e não devem ser usadas como nome de variáveis ou funções. Não é possivel forçar outro valor.


7. Qual a saída do seguinte trecho de código? Se algum erro aparecer, diga qual o erro e o motivo dele. (2 pt)
```python
a = "10"
int = a
print(a, int)
print(int(a))
```
10, a
erro pq a é string


## Prático
8. dado um retângulo de largura 10cm e altura 23.5 cm, escreva um código que calcula a sua área e printe-a. use variáveis separadas (ou seja, declare `largura`, `altura` e `area` separadamente) (1 pt)

def area(a, l):
    area_ret = a * l
    print(area_ret)
a = 10
l = 23.5
area(a, l)


9. há algum erro no código abaixo? se sim, como você o corrigiria? (1 pt)

```python
print("teste"*2)
print(c)
c = "teste"
```
Não dá pra printar c se foi declarado antes do print, precisa declarar antes.
print("teste"*2)
c = "teste"
print(c)


10. adicione comentários e renomeie variáveis e funções para deixar o código abaixo mais claro. ATENÇÃO: em vez de editar o trecho de código, crie a cópia editada abaixo.
```python
def f(a,b):
	c = 0
	for i in range(b):
		c += g(a)
return c

def g(a):
	return a**2
```
```python
def f(a,b):
'''Calcula soma de cada item dentro de b, com a potência de a e retorna o resultado final'''

	count = 0
	for i in range(b):
		count += calcula_potencia(a)
return count

def calcula_potencia(a):
	'''Calcula potência de a'''
	return a**2
```