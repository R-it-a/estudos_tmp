import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
# Perguntas:

<<<<<<< HEAD


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

#4. qual o total de livros disponíveis?

total_estoque = df['In Stock'].sum()
print(total_estoque)

#5. qual o livro mais caro? e o mais barato?
mais_caro = df['Price'].max()
print(mais_caro)
mais_barato = df['Price'].min()
print(mais_barato)

#6. qual é o gênero mais caro em média?

df['Price'] = df['Price'].str.replace('£', '').astype(float)

genre_price = df.groupby('Category')['Price'].mean()
if genre_price.empty:
    print("Fodeu")
else:
    expensive_genre = genre_price.idxmax()
    cheap_genre = genre_price.idxmin()

    expensive_genre_ratings = f'{genre_price[expensive_genre]:.2f}'
    cheap_genre_ratings = f'{genre_price[cheap_genre]:.2f}'

    print(f"The genre with biggest price is: {expensive_genre} with {expensive_genre_ratings}")
    print(f"The genre with cheapest price is: {cheap_genre} with {cheap_genre_ratings}")

# 7. com é o gênero com mais livros disponveís?
df['Category'] = df['Category'].str.strip()  # Remover espaços em branco ao redor
df = df[df['Category'] != 'Add a comment']
print(df['Category'].unique())



df['Star Rating'] = df['Star Rating'].astype(int)

plt.figure(figsize=(8, 6))
df['Star Rating'].plot(kind='hist', bins=5, edgecolor='pink', color='purple')
plt.xlabel('Star Rating')
plt.ylabel('Distribuition of Star Ratings')
#plt.show()

#9. monte um gráfico com as notas por gênero
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:pink'
ax1.set_xlabel('Category')
ax1.set_ylabel('Average Star Rating', color=color)
genre_ratings.plot(kind='bar', ax=ax1, color=color, position=0, width=0.4)
ax1.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Average Star Rating and Price by Category')
plt.show()

#10. monte um gráfico com distribuição de preços
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=10, color='pink', edgecolor='black')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.title('Distribution of Prices')
plt.show()


#11. você acha que com as features disponíveis, é possível de fazer um
#   classificador de nota dado o livro? justifique.
#Sim, podemos prever tanto o preço, quanto a nota q um livro vai ter baseada nas features q temos por categoria,
#o que nao quer dizer q conseguiriamos capturar subjetividades de cada livro novo lançado, e de outliers, ou seja, não há garantias de precisão e afins

# Codificação das categorias em variáveis dummy
df = pd.get_dummies(df, columns=['Category'], drop_first=True)

# Dividir os dados em features (X) e alvo (y)
X = df[['Price', 'In Stock'] + [col for col in df.columns if col.startswith('Category_')]]
y = df['Star Rating']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar um classificador Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = clf.predict(X_test)

# Avaliar o modelo
print(classification_report(y_test, y_pred))
=======
if __name__ == "__main__":
    # boa sorte!


>>>>>>> 007d8af (git push)
