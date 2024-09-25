# Capítulo 2


## Teórico
1. Como você adiciona um comentário em um código Python? Como você adiciona um comentário que engloba múltiplas linhas? (0.5 pt)

2. O que é um erro de sintaxe? O que é um erro de runtime? O que é um erro semântico? Dê um exemplo de cada. (1.5 pts)

3. Como você importa um módulo? É possível importar uma função específica de um módulo em vez de ele todo? Se sim, como? (1 pt)

4. O que é um argumento de uma função? (1 pt)

5. Qual é a saída? (1 pt)
	a) print("número"); print(1/2)
	b) print("número", 1+1)
	c) num = 6; print(f"número {num%3})
	d) num = 4; print("numero {}".format(num + 3))

6. O que é um palavra reservada na linguagem (keyword)? Você consegue sobrescrever o seu valor? (1 pt)

7. Qual a saída do seguinte trecho de código? Se algum erro aparecer, diga qual o erro e o motivo dele. (2 pt)
```python
a = "10"
int = a
print(a, int)
print(int(a))
```

## Prático
8. dado um retângulo de largura 10cm e altura 23.5 cm, escreva um código que calcula a sua área e printe-a. use variáveis separadas (ou seja, declare `largura`, `altura` e `area` separadamente) (1 pt)

9. há algum erro no código abaixo? se sim, como você o corrigiria? (1 pt)

```python
print("teste"*2)
print(c)
c = "teste"
```

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
