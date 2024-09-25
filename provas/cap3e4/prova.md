1. qual a saída do código abaixo? se houver algum erro/problema, descreva-o.
 a)
 ```python
 def repete_a(palavra, n_vezes):
 	for i in n_vezes:
		print(palavra)

 print(repete_a("oi", 2))
 ```

 b)
 ```python
 def repete_b(palavra, n_vezes):
 	for i in range(n_vezes):
		print(palavra)

 print(repete_b("oi", -1))
 ```
 c)
 ```python
 def repete_c(palavra, n_vezes=5):
 	for i in range(n_vezes):
		print(palavra)

 print(repete_c("oi"))
 ```

2. no código acima, existe alguma restrição quanto ao tipo das variáveis? qual é
   a saída se chamarmos a função como
   a) `repete_a(-1, 1)`?
   b) `repete_b("palavra", "ok")`
   c) `repete_c(2/3, 2)`


3. por que usamos funções? qual é a melhor forma de debugar uma função?

4. considere o seguinte trecho de código:
```python
def nome_completo(nome, sobrenome):
	nome = "Giovana"
	return f"{nome} {sobrenome}"


nome = "Rita"
sobrenome = "Farias"

print(nome_completo(nome, sobrenome))
print(nome)
```

qual a saída será printada na tela? por quê? justifique sua resposta e relacione
ela ao conceito de escopo de variável.

5. agora, considere o seguinte código
```python
def nome_completo():
	return f"{nome} {sobrenome}"


nome = "Rita"
sobrenome = "Farias"

print(nome_completo(nome, sobrenome))
print(nome)
```

qual é a saída? por quê? justifique novamente relacionando ao conceito de escopo
de variável.

5. escreva uma função chamada "fatorial" que recebe um inteiro "n" e retorna o
   seu fatorial (n x n-1 x n-2 ...). quanto é o fatorial de 23?

6. escreva uma função chamada "triangulo" que receberá uma string e um inteiro.
   sua função então desenhará uma pirâmide com a altura dada, feita unicamente
   de cópias da sua string. por exemplo
   ```python
   triangulo(5, "L")

   # saída:
   L
   LL
   LLL
   LLLL
   LLLLL
   ```

7. o que significa dizer que você está "refatorando" um código? por que você
   faria isso?


8. o código abaixo printa a tabuada do 2 até 10. refatore o código para que ele printe a tabuada de qualquer número até qualquer número.
	mude nomes de variáveis e funções que achar conveniente. adicione
	docstrings explicando o que a função faz e quais seus parâmetros e tipos.
   ```
   def t():
   		for i in range(10):
			print("2 * 10 = ", i*10)

   t()
   ```
