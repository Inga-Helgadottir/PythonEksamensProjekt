import pandas as pd
from DataCode.addColumnWithSentenceInfo import makeSentenceInfo

def makeMovieData():
    # the path to the original movie data
    originalMovieData = "DataFiles/MoviesOriginal.csv"

    # the location where i want to put the data after i changed it to fit my project
    myMovieData = "DataFiles/myMovieData.csv"

    # read the csv file into a DataFrame and only keep the columns movie_title, genre, studio_name, directors
    df = pd.read_csv(originalMovieData, usecols = ["movie_title", "genre", "studio_name", "directors"], 
              skipinitialspace=True)

    # rename all the columns
    df_new = df.rename(columns={"movie_title": "guessWord", "genre": "genreHint", "directors": "directorsHint", "studio_name": "studioHint"})

    # adding a new column with sentence info (this becomes = 4_7)
    df_new['sentenceInfo'] = df_new['guessWord'].apply(makeSentenceInfo)

    # save my movie code to its own csv file
    with open(myMovieData, "w", newline='') as f:
        # enters the code into a DataFrame
        resultsDF = pd.DataFrame.from_dict(df_new)
        # changes the data to csv form and gives each row an id
        resultsDF_CSV = resultsDF.to_csv(index=True)
        # write the content to the file
        f.write(resultsDF_CSV)