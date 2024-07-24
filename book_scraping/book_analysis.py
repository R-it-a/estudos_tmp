import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Perguntas:

#4. qual o total de livros disponíveis?
#5. qual o livro mais caro? e o mais barato?
#6. qual é o gênero mais caro em média?
#7. com é o gênero com mais livros disponveís?
#8. plote um histograma que mostre a distribuição de notas
#9. monte um gráfico com as notas por gênero
#10. monte um gráfico com distribuição de preços
#11. você acha que com as features disponíveis, é possível de fazer um
#   classificador de nota dado o livro? justifique.


df = pandas.read_csv("books.csv")
#1. qual o total de livros?
row_count = len(df)
print(f"There are {row_count} books.")

#2. qual o livro com mais estoque?

print(df['In Stock'].max())
print(df.nlargest(1, ['In Stock']))

#3. qual o gênero de livro com melhor avaliação na média? e qual o gênero com
#   pior avaliação?

rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

df['Star Rating'] = df['Star Rating'].map(rating_map)

genre_ratings = df.groupby('Category')['Star Rating'].mean()

if genre_ratings.empty:
    print("Fodeu")
else:
    best_genre = genre_ratings.idxmax()
    worst_genre = genre_ratings.idxmin()

    best_genre_ratings = f'{genre_ratings[best_genre]:.2f}'
    worst_genre_ratings = f'{genre_ratings[worst_genre]:.2f}'

    print(f"The genre with best rating is: {best_genre} with {best_genre_ratings}")
    print(f"The genre with worst rating is: {worst_genre} with {worst_genre_ratings}")
