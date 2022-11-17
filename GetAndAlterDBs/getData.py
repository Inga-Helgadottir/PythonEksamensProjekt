import pandas as pd

movieData = "../data/Movies.csv"

df = pd.read_csv(movieData, usecols = ["movie_title", "genre", "studio_name", "directors"])

df_new = df.rename(columns={"movie_title": "guessWord", "genre": "genreHint", "directors": "directorsHint", "studio_name": "studioHint"})

# print(df_new)
with open("../data/MyMovieDB.csv", "w") as f:
    resultsDF = pd.DataFrame.from_dict(df_new)
    resultsDF_CSV = resultsDF.to_csv(index=False)
    f.write(resultsDF_CSV)

####################################################################################################

import requests
import json

response = requests.get("https://rickandmortyapi.com/api/character")
        
results = response.json()["results"]

with open("../data/rickAndMortyDB.csv", "w") as f:
    resultsDF = pd.DataFrame.from_dict(results)
    resultsDF_CSV = resultsDF.to_csv(index=False)
    f.write(resultsDF_CSV)

df = pd.read_csv("../data/rickAndMortyDB.csv", usecols = ["name", "gender", "species", "origin"])

def reformatOrigin(origin):
    
    test = origin.split("'")[3].strip()
    
    return test

df['origin'] = df['origin'].apply(reformatOrigin)
df_new = df.rename(columns={"name": "guessWord", "gender": "genderHint", "species": "speciesHint", "origin": "originHint"})

with open("../data/MyRickAndMortyDB.csv", "w") as f:
    resultsDF = pd.DataFrame.from_dict(df_new)
    resultsDF_CSV = resultsDF.to_csv(index=False)
    f.write(resultsDF_CSV)