import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configurações de autenticação
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='SEU_CLIENT_ID',
    client_secret='SEU_CLIENT_SECRET',
    redirect_uri='http://localhost:8888/callback',
    scope='playlist-modify-public'
))

# Lista de bandas
bands = [
    "The Skatalites", "The Wailers", "Toots and the Maytals", "The Paragons", "The Ethiopians",
    "The Pioneers", "Prince Buster", "Derrick Morgan", "The Maytals", "The Heptones",
    "The Clarendonians", "The Melodians", "The Techniques", "The Blues Busters",
    "Desmond Dekker & The Aces", "Justin Hinds & The Dominoes", "The Gaylads",
    "Alton Ellis & The Flames", "Tommy McCook & The Supersonics", "Baba Brooks Band"
]

# Lista para armazenar IDs das músicas
track_ids = []

# Busca as 5 músicas mais populares de cada banda e 2 recomendações para cada música
for band in bands:
    # Busca o ID do artista
    artist_results = sp.search(q=f'artist:{band}', type='artist', limit=1)
    if artist_results['artists']['items']:
        artist_id = artist_results['artists']['items'][0]['id']
    else:
        print(f"Artista não encontrado: {band}")
        continue

    # Obtém as top 5 faixas do artista
    top_tracks = sp.artist_top_tracks(artist_id, country='US')['tracks'][:5]
    for track in top_tracks:
        track_ids.append(track['id'])

        # Obtém 2 recomendações baseadas na faixa atual
        recommendations = sp.recommendations(seed_tracks=[track['id']], limit=2, country='US')
        for rec in recommendations['tracks']:
            track_ids.append(rec['id'])

# Cria uma nova playlist
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user=user_id, name='Jamaican Ska Recommendations', public=True, description='5 top ska tracks from legendary bands + 2 recommendations for each')

# Função para dividir a lista em lotes de no máximo 100 itens
def chunked(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]

# Adiciona as músicas à playlist em lotes
for batch in chunked(track_ids, 100):
    sp.playlist_add_items(playlist_id=playlist['id'], items=batch)

print(f"Playlist criada com sucesso! Confira no seu Spotify: {playlist['external_urls']['spotify']}")
