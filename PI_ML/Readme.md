<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

 

<hr>  

## Contenido del README

- [Descripción del Problema](#descripción-del-problema)
- [Contexto y desarrollo](#Contexto-y-desarrollo)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-(EDA))
- [Modelo de Aprendizaje Automático](#modelo-de-aprendizaje-automático)
- [Desarrollo de la API](#Desarrollo-de-la-API)
- [Transformaciones](#Transformaciones)
- [Video de Demostración](#video-de-demostración)
- [Repositorio](#repositorio)
- [Fuentes de Datos](#fuentes-de-datos)

## Descripción del Problema

Steam necesitaba un sistema de recomendación de videojuegos para sus usuarios. Los datos iniciales eran desafiantes, con datos crudos y poco limpios. Como MLOps Engineer se realizaron tareas de Data Engineering y se creo un MVP para abordar este problema, ademas de otras funciones.
## Contexto y desarrollo

Este proyecto de Machine Learning contempla desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

## Exploratory Data Analysis (EDA)

Se ha realizado un análisis exploratorio de datos para comprender mejor el dataset, incluyendo:

- Identificación de relaciones entre variables.
- Identificación de outliers o anomalías.
- Exploración de patrones interesantes.
- Analisis de datos a traves del tiempo.

### Modelo de Aprendizaje Automático

Tambien implementa un sistema de recomendación de videojuegos utilizando el enfoque de Item-Item:

- **Ítem-Ítem**: Este sistema recomienda juegos similares a un juego dado.

- Se ha creado la columna 'sentiment_analysis' aplicando análisis de sentimiento con NLP, (NLTK)
- La columna 'sentiment_analysis' reemplaza la columna 'user_reviews.review' según lo especificado.

 

### Desarrollo de la API

- Se han creado las siguientes funciones para los endpoints de la API:


+ def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.
  
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,
			     "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **UsersWorstDeveloper( *`año` : int* )**:
   Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **sentiment_analysis( *`empresa desarrolladora` : str* )**:
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total 
    de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor. 

Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}
<br/>


### Transformaciones 

- Se ha realizado la lectura de los datasets en el formato JSON.
- Se ha realizado transformacion de datos, limpieza, imputacion de datos faltantes, etc.
- se han exportado como parquet.
- Las columnas y filas innecesarias se han eliminado para optimizar el rendimiento de la API y el entrenamiento del modelo.



## Video de Demostración

Puedes ver una demostración de la API y el modelo de recomendación en funcionamiento en el siguiente enlace: [Enlace al Video](https://www.youtube.com/)

## Repositorio

El código fuente de este proyecto se encuentra en el siguiente repositorio: [Enlace al Repositorio](https://github.com/juan123531/)

## Fuentes de Datos

- Datasets: [Enlace al Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/-Docker-333333?style=flat&logo=docker)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)

