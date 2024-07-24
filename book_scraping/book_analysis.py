import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Perguntas:
#3. qual o gênero de livro com melhor avaliação na média? e qual o gênero com
#   pior avaliação?
#4. qual o total de livros disponíveis?
#5. qual o livro mais caro? e o mais barato?
#6. qual é o gênero mais caro em média?
#7. com é o gênero com mais livros disponveís?
#8. plote um histograma que mostre a distribuição de notas
#9. monte um gráfico com as notas por gênero
#10. monte um gráfico com distribuição de preços
#11. você acha que com as features disponíveis, é possível de fazer um
#   classificador de nota dado o livro? justifique.


df = pandas.read_csv("SCB.csv")
#1. qual o total de livros?
row_count = len(df)
print(f"There are {row_count} books.")

#2. qual o livro com mais estoque?



#if __name__ == "__main__":
# boa sorte!


