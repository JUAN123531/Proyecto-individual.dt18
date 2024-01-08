from fastapi import FastAPI
import pandas as pd
from recommendation import cosine_sim



app = FastAPI()


# 1


@app.get('/genero /')
def PlayTimeGenre(year : str):
    ''' Debe devolver año con mas horas jugadas para dicho género.
        Ejemplo de retorno: 
       {"Año de lanzamiento con más horas jugadas para Género X" : 2013}'''
    df = pd.read_parquet(r'./Data/endpoint1.parquet.gzip')
    # Verifica si el año ingresado existe en el DataFrame
    if year not in df.columns:
        return "Invalid year"
     # Multiplicamos la columna del genero por la columna de playtime_forever
    genre_playtime = df[genre] * df['playtime_forever']
    
    # Calcula el total de horas jugadas en el genero
    total_genre_playtime = genre_playtime.sum()

    # Lista de generos pertenecientes al DataFrame
    genre_columns = [
        'Action', 'Indie', 'Adventure', 'Casual', 'Fighting', 'Multiplayer',
        'Puzzle', 'RPG', 'Sandbox', 'Shooter', 'Simulation', 'Singleplayer',
        'Sports', 'Strategy', 'Survival', 'Zombies'
    ]

    # Calcula el total de horas jugadas en cada genero
    total_playtimes = {
        genre: (df[genre] * df['playtime_forever']).sum()
        for genre in genre_columns
    }

    # Ordena los generos de mayor a menor
    sorted_genres = sorted(total_playtimes.items(),
                           key=lambda x: x[1],
                           reverse=True)

    # Busca el puesto del genero ingresado
    rank = 1
    for genre, playtime in sorted_genres:
        if genre == genre:
            return rank
        rank += 1
    # Filtra el DataFrame por el genero ingresado
    genre_df = df[df[year] == 1]

    # Ordera el DataFrame por playtime_forever
    genre_df = genre_df.sort_values(by='playtime_forever',
                                           ascending=False)
    return {
      "Usuario con más horas jugadas para " : genre_df,'es' year
    }

# 2


@app.get('/UserForGenre/')
def UserForGenre(genre : str) :
    """
 Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
 Ejemplo de retorno:
  {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
    """
    df = pd.read_parquet(r'./Data/endpoint2.parquet.gzip')
    user_data = df[df['genre'] == genre]

    # Calcula total gastado por usuario
    total_spent = user_data['price'].sum()
    
    total_items = user_data['items_count'].sum()

    return {
       
       'Usuario con más horas jugadas para Género X':total_spent,
       'Horas jugadas':total_items
      
    }


# 3


@app.get('/UsersRecommend/')
def UsersRecommend(year : str ):
    """
    Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    """
    df = pd.read_parquet(r'./Data/endpoint3.parquet.gzip')
    fil_end4 = df[(df.year == year)]
    f = pd.DataFrame(
        fil_end4.groupby(['user_id',
                          'year'])['id'].count().sort_values(ascending=False))
    f.reset_index(inplace=True)
    s = f.head(3)
    return {
        'Puesto 1': s.year.to_list(),
        'Puesto 2': s.id.to_list(),
        'Puesto 3': s.id.to_list()
       
    }
    
   
# 4


@app.get('/UsersWorstDeveloper/')
def  UsersWorstDeveloper(year: int):
    """
   Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
   Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    """
    df = pd.read_parquet(r'./Data/endpoint4.parquet.gzip')
    fil_end4 = df[(df.year == year)]
    f = pd.DataFrame(
        fil_end4.groupby(['user_id',
                          'year'])['id'].count().sort_values(ascending=True))
    f.reset_index(inplace=True)
    s = f.head(3)
    return {
        'Puesto 1': s.year.to_list(),
        'Puesto 2': s.id.to_list(),
        'Puesto 3': s.id.to_list()
       
    }
  

# 5

@app.get('/sentiment_analysis/')
def sentiment_analysis(empresa_desarrolladora : str):
     """
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un ]}análisis de sentimiento como valor.
Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278 """
     df = pd.read_parquet(r'./Data/endpoint5.parquet.gzip')
     fil = df[df.reviews_item_id == reviews_item_id]
    return {
    
        'Negativo'= fil.negativo.to_list()[0],
        'Neutral'=fil.neutral.to_list()[0]
        'Positivo'= fil.positivo.to_list()[0],
    }
  
# ML
@app.get('/recomendacion_juego/{id_del_producto}')
def recomendacion_juego(id_del_producto: str):
     ''' 
     Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
      '''
     games_model= pd.read_parquet(r'./Data/endponint6_with_reco.parquetparquet.gzip')
    #def recomendacion_juego( id de producto ): Ingresando el id de producto,
    # deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
     item_indice = games_model[games_model['id'] == id_del_producto].index[0] # Extraemos el indice de nuestro juego en nuestro dataset de juegos
     items_similares = list(enumerate(cosine_sim[item_indice])) # Conseguimos nuestros items similares
     recommended_items = sorted(items_similares, key=lambda x: x[1], reverse=True) # Ahora ordenamos para saber nuestros items mas recomendados
     indices = [index for index, _ in recommended_items[1:10]] # Extraemos los indices de los juegos
     recommended_items = games_model.iloc[indices]['id'].tolist() # Convertimos a listas con nuestros ids, (podriamos poner nuestros app_name)
     recomedations = ""
     for i in recommended_items[:5]:
        recomedations+=f'<p>{games_model[games_model.id == i].app_name.tolist()[0]}</p>'
     return recomedations # Retornamos los primeros 5



