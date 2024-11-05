1. Em Python, é aceitável uma função sem retorno? Quais casos você acha que isso pode ser útil?
R: Sim, podemos ter funções sem retorno, ela retorna um None nesse caso, mas podemos ter prints no lugar. Algumas vezes pode ser necessário apenas printar algum valor.


2. Escreva abaixo uma função que receba dois números e retorne o máximo entre eles
```python
def max_dois_numeros(a,b):
```
R:
def max_dois_numeros(a,b):
    if a > b:
        return a
    else:
        return b

3. O que é uma função booleana? Qual a vantagem de ter algo assim?
R: Uma função booleana é uma função quer retorn True or False. A vantagem se encontra em poder checar se expressões ou condições são verdadeiras, e em seguida, utilizá-las em outras
partes do programa, que dependam do True or False retornado.



4. Escreva uma função booleana esta_entre(x,y,z), que retorna "True" se x < y < z e "False" caso contrário.
R:

def esta_entre(x,y,z):
    return x < y < z

5. O que é uma função pura?
R: É uma função cuja "função" é apenas retornar um valor, e nada mais.

6. Por que é importante validar se os tipos das variáveis que estamos recebendo de fato é o que esperamos? Você consegue pensar em um exemplo prático do seu trabalho?
R: A importância de validar está no fato de que as vezes a lógica da função ou de outras partes do código não retorna o que esperamos, é importante sempre checar para garantir
que não caimos em erros de lógica, sintaxe, etc. Isso vale para o valor em si, não só para seu tipo. Mas o tipo errado pode ter implicações diversar e indesejadas, por exemplo, no meu
digníssimo trabalho, coom frequência preciso gerar e organizar dados em dataframes, e neste processo, é comum que o spark ou o pandas recebam datas como string. 
Nas diversas vezes que não percebi isso, todo o cálculo dos meus modelos ficam prejudicados. Agora, usamos testes finais antes de salvar o dataframe e gerar modelo, para garantir
que os tipos das variáveis são os que queremos.

7. Escreva uma função `primeiro_ultimo_char(texto)` que retorne o primeiro e último caracteres de uma string. 
Exemplo de entrada: "giovana"
Exemplo de saída: "ga"

Exemplo de entrada: "sofia rita e giovana"
Exemplo de saída: "sa"

Exemplo de entrada: "s"
Exemplo de saída: "Entrada precisa ter pelo menos 2 caracteres" 

R:
def primeiro_ultimo_char(texto):
    caracteres = []
    caracteres.append(texto[0])
    caracteres.append(texto[-1])
    wanted_values = ''.join(caracteres)
    print(wanted_values)

8. (desafio) Escreva uma função fatorial de maneira recursiva. 
def facto(n):
    if n == 0:
        return 1
    else:
        fatorial = facto(n-1)
    return n * fatorial
