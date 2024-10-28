1. qual a saída do código abaixo? se houver algum erro/problema, descreva-o.
 a)
 ```python
 def repete_a(palavra, n_vezes):
 	for i in n_vezes:
		print(palavra)

 print(repete_a("oi", 2))
 ```
R: oioi
Incorreto. Um `for` não aceita um inteiro como iterador. Esse código dá um erro
do tipo `TypeError: 'int' object is not iterable`


 b)
 ```python
 def repete_b(palavra, n_vezes):
 	for i in range(n_vezes):
		print(palavra)

 print(repete_b("oi", -1))
 ```
Não vai printar oi porque -1 não é valido para iterar.
Meio certo. Não vai printar, mas não vai dar nenhum erro. Em teoria, o -1 é
válido pra iterar, mas o range(-1) é um iterador vazio.

 c)
 ```python
 def repete_c(palavra, n_vezes=5):
 	for i in range(n_vezes):
		print(palavra)

 print(repete_c("oi"))
 ```
oioioioioi
Incorreto. O correto é
oi
oi
oi
oi
oi
porque não estamos concatenando e cada print printa em uma nova linha.

2. no código acima, existe alguma restrição quanto ao tipo das variáveis? qual é
   a saída se chamarmos a função como
   a) `repete_a(-1, 1)`?
	   Aqui nao vai iterar, não sei explicar o porque

	   Incorreto. Realmente não vai printar, mas não é por causa do tipo de
	   variável, mas sim por causa do erro descrito no exercício 1.a)

   b) `repete_b("palavra", "ok")`
	   ok is not iterable

	   Meio certo. O problema é que o ok não é convertido pra inteiro dentro do
	   range. O erro que o interpretador dá é `TypeError: 'str' object cannot be interpreted as an integer` (vc não precisava saber esse erro).


   c) `repete_c(2/3, 2)`
	   Aqui nao vai iterar, não sei explicar o porque

	   Incorreto. Vai printar
	   0.6666
	   0.6666


3. por que usamos funções? qual é a melhor forma de debugar uma função?
Funções são eficientes para encapsular códigos, e evitar repetições. Caso existam situações que você precisa repetir o mesmo processo mais deuma vez,
o ideal é fazer uma função.

Meio-certo. Não respondeu a segunda parte da pergunta.


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

Giovana Farias
Rita

A variável que está dentro da função, é uma variável local enquanto Rita está fora da função. Quando chamamos a função pra printar,
mesmo colocando nome como Rita, ela passe pela variavel interna e transforma Rita em Giovana.

Correto.

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

nesse caso, o returno f não consegue ler as variáveis que estão fora da função, e também não foram estabelecidas como parametros.
o segundo print funciona bem, pq é uma variável global que está fora da função.

Correto.

5. escreva uma função chamada "fatorial" que recebe um inteiro "n" e retorna o
   seu fatorial (n x n-1 x n-2 ...). quanto é o fatorial de 23?

def fatorial(n):
    return n * n - 1 * n - 2

print(fatorial(23))

Incorreto. A sua função retorna apenas `23*22*21` o que é diferente de 23!.


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
def triangulo(string, H):
    for i in range(H):
        print(string * i)

Meio certo. Os parâmetros estão ao contrário do que o definido no exercício e
seu triângulo tem um andar a menos do que deveria.


7. o que significa dizer que você está "refatorando" um código? por que você
   faria isso?

Refatorar é tornar o código melhor, mais rápido, mais conciso, é um processo semelhante a revisar, mas buscando melhorias.

80% certo. Eu adicionaria um comentário a respeito da legibilidade de código e
que isso é importante principalmente pra outras pessoas que vão ler esse código
e pra você do futuro.


8. o código abaixo printa a tabuada do 2 até 10. refatore o código para que ele printe a tabuada de qualquer número até qualquer número.
	mude nomes de variáveis e funções que achar conveniente. adicione docstrings explicando o que a função faz e quais seus parâmetros e tipos.
   ```
   def t():
   		for i in range(10):
			print("2 * 10 = ", i*10)

   t()
   ```
def t(number_1, range_n):
    for i in range(range_n):
        count = number_1 * i
        print(f"{number_1} x {i} = {count}")

t(5, 5)

Meio certo. As variáveis não estão bem nomeadas e faltou documentar o que são as
variáveis e pra que elas servem. A função também não foi renomeada (ela poderia se chamar, por exemplo, tabuada). A pergunta que você tem que se fazer é: se eu ler
esse código assim, eu vou entender?
