import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer # Importamos nuestro CountVectorizer de sklearn
from sklearn.metrics.pairwise import cosine_similarity # Y nuestro coseno de simil
games_model = pd.read_parquet(r'./Data/endpoint6.parquet.gzip')


# %%
generos_a_excluir = [ # Creamos una lista de los generos menos vistos en el dataset, esto lo hacemos para reducir el tamaño
                      # del dataset por motivos de rendimiento, aunque por el otro lado perdemos precision en nuestro modelo
 'Simulation',
 'Strategy',
 'Free to Play',
 'RPG',
 'Sports',
 '[]',
 'Racing',
 'Early Access',
 'Massively Multiplayer',
 'Animation &amp; Modeling',
 'Video Production',
 'Utilities',
 'Web Publishing',
 'Education',
 'Software Training',
 'Design &amp; Illustration',
 'Audio Production',
 'Photo Editing',
 'Accounting']


# %%
for i in generos_a_excluir:
    games_model = games_model[games_model['genres'] != i] # Eliminamos los juegos que sean de esos generos


# %%
games_model.dropna(inplace=True) # Eliminamos valores faltantes
co = CountVectorizer(max_features=9000, stop_words='english') # Creamos nuestro contador de vectores con un maximo de 7000 regs
                                                              # Tambien aprovechamos y por las dudas, eliminamos nuestras stopwords


# %%
vector = co.fit_transform(games_model['genres']).toarray() # Creamos nuestro vector, entrenandolo con nuestra principal variable predictora, generos



# %%
co.get_feature_names_out() # Extraemos los nombres de los features


# %%
cosine_sim = cosine_similarity(vector)


# %%
games_model.to_parquet(r'./Data/endponint6_with_reco.parquet.gzip', compression='gzip') # Exportamo
