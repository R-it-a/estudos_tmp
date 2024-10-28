1. qual a saída do código abaixo? se houver algum erro/problema, descreva-o.
 a)
 ```python
 def repete_a(palavra, n_vezes):
 	for i in n_vezes:
		print(palavra)

 print(repete_a("oi", 2))
 ```
R: A saída é: obj int is not iterable. Isso acontece quando colocamos um número diretamente no for, a melhor solução conhecida pela minha pessoa é usar um range, então:
def repete_a(palavra, n_vezes):
    for i in range(n_vezes):
        print(palavra)

print(repete_a("oi", 2))
cuja saída será: oi printado duas vezes em linhas diferentes, nesse caso também retorna none.

 b)
 ```python
def repete_b(palavra, n_vezes):
    for i in range(n_vezes):
	    print(palavra)

print(repete_b("oi", -1))

 ```
R: Esse print apenas retorna None. A string não é printada porque a função range só funciona em ordem ascendente quando é usado um único parâmetro.


 c)
 ```python
 def repete_c(palavra, n_vezes=5):
 	for i in range(n_vezes):
		print(palavra)

 print(repete_c("oi"))
 ```
R: Neste caso, a função funciona normalmente, porque o parâmetro n_vezes tem um valor padrão mesmo quando não é estabelecido na hora de chamar a função, então são printados 5 ois em linhas diferentes, e retorna None no fim.


2. No código acima, existe alguma restrição quanto ao tipo das variáveis? qual é a saída se chamarmos a função como
    Pela forma como o corpo da função foi deficinido, temos um contrato que estabelece que deve ser passado um valor que será printado, e nesse caso o tipo pode variar, mas o segundo parâmetro precisa ser um número int, o qual será iterado.

   a) `repete_a(-1, 1)`?
    R: Neste caso, a iteração não ocorrerá, porque a função repete_a não tem a função range. Então o erro int obj is not iterable ocorre.

   b) `repete_b("palavra", "ok")`
   R: O segundo parâmetro precisa ser um int. Como passamos uma string, dá o erro str object cannot be interpreted as an interger.

   c) `repete_c(2/3, 2)`
    R: Aqui a função funciona normalmente, printa duas vezes em linhas diferentes o resultado da divisão 2/3. Como não foi usado print, não retorna None na última linha.


3. por que usamos funções? qual é a melhor forma de debugar uma função?
Funções são usadas para evitar repetições de códigos, para facilitar a reutilização de trechos de código, e também ajuda a nomear pedaços de código, o que torna o script mais limpo e compreensível.
Funções tornam um código mais fácil de debugar, porque nos permite dividi-lo em pedaços menores, e executar em partes.

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

Essa saída foi printada porque quando estabelecemos dentro da função a variável local nome, mesmo que passemos um nome como parâmetro ao chamar a função, a variável local é utilizada como prioridade.
Então o parâmetro válido se torna apenas o sobrenome. O segundo print é feito direto, sem utilizar a função e funciona com a varíavel global, printando Rita normalmente.
A variável que está dentro da função, é uma variável local enquanto Rita está fora da função. Variáveis locais deixam de existir fora da função, mesmo que eu tentasse imprimir Giovana, não seria possível.
Já as variáveis globais podem ser usadas dentro e fora da função.

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

R: Temos um erro aqui, TypeError. Isso ocorre porque não foram estabelecidos parâmetros na função, mas passamos dois, que não serão aceitos, não está no contrato.
O segundo print mostraria a variável global Rita, porém o programa não chega nele, uma vez que para com o erro descrito anteriormente.

Correto.

5. escreva uma função chamada "fatorial" que recebe um inteiro "n" e retorna o
   seu fatorial (n x n-1 x n-2 ...). quanto é o fatorial de 23?

def fatorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    print(factorial)
print(fatorial(23))

Correto

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
def triangulo(string, h):
    for i in range(h+1):
        print(string * i)
triangulo("h", 5)

O código tá certo, mas eu tiraria 0.25 porque você inverteu a ordem dos
parâmetros. A função foi definida como triangulo(5, "L") e você criou como
triangulo(string, h).
Relacionado, mas sem tirar qualquer pontuação: se você decidir escrever
seu código em ingles, use todos os nomes em ingles (ex triangle em vez de
triangulo). Se decidir usar português, usa tudo em pt também).


7. o que significa dizer que você está "refatorando" um código? por que você
   faria isso?

Refatorar é tornar o código melhor, mais rápido, mais conciso, é um processo semelhante a revisar, mas buscando melhorias.

Correto. Adicionaria que refatorar é bom pra você mesma do futuro, mas isso não
tira nenhum ponto.

8. o código abaixo printa a tabuada do 2 até 10. refatore o código para que ele printe a tabuada de qualquer número até qualquer número.
	mude nomes de variáveis e funções que achar conveniente. adicione
	docstrings explicando o que a função faz e quais seus parâmetros e tipos.
   ```
   def t():
   		for i in range(10):
			print("2 * 10 = ", i*10)

   t()
   ```
def t(number_1, number_2):
'''

Recebe dois números int como parâmetros e printa a tabuada do primeiro número até o range do segundo número.

'''
    for i in range(number_2 + 1):
        count = number_1 * i
        print(f"{number_1} x {i} = {count}")

t(10, 8)

Correto
