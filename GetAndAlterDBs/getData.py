import pandas as pd

movieData = "../data/Movies.csv"

df = pd.read_csv(movieData, usecols = ["movie_title", "genre", "studio_name", "directors"])

df_new = df.rename(columns={"movie_title": "guessWord", "genre": "hint", "directors": "hint2", "studio_name": "hint3"})

print(df_new)
####################################################################################################

rickAndMortyUrl = "https://rickandmortyapi.com/"