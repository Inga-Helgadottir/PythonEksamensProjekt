import pandas as pd
import requests
from DataCode.addColumnWithSentenceInfo import makeSentenceInfo

def makeRickAnMortyData():
    # the url to the Rick and Morty API
    originalRickAndMortyUrl = "https://rickandmortyapi.com/api/character"

    # the location where i want to put the original data
    originalRickAndMortyData = "DataFiles/RickAndMortyFromOriginal.csv"

    # the location where i want to put the data after i changed it to fit my project
    myRickAndMortyData = "DataFiles/myRickAndMortyData.csv"

    # getting the data from the API
    response = requests.get(originalRickAndMortyUrl)

    # getting only the content inside results        
    results = response.json()["results"]

    # save original code to its own csv file
    with open(originalRickAndMortyData, "w", newline='') as f:
        # enters the code into a DataFrame
        resultsDF = pd.DataFrame.from_dict(results)
        # turns the json data to csv
        resultsDF_CSV = resultsDF.to_csv(index=True)
        # write the content to the file
        f.write(resultsDF_CSV)

    # read the csv file into a DataFrame and only keep the columns name, gender, species, origin
    df = pd.read_csv(originalRickAndMortyData, usecols = ["name", "gender", "species", "origin"], 
              skipinitialspace=True)

    # the origin column gives a weird result
    def reformatOrigin(origin):
        # splits the column where the symbol ' appears, keep only the 4th and strips the empty spaces
        splitOrigin = origin.split("'")[3].strip()
        return splitOrigin

    # apply the changes to the origin column
    df['origin'] = df['origin'].apply(reformatOrigin)

    # rename all the columns and save in a new dataframe
    df_new = df.rename(columns={"name": "guessWord", "gender": "genderHint", "species": "speciesHint", "origin": "originHint"})

    # adding a new column with sentence info (this becomes = 4_7)
    df_new['sentenceInfo'] = df_new['guessWord'].apply(makeSentenceInfo)

    # save the changed data to its own csv file
    with open(myRickAndMortyData, "w", newline='') as f:
        # enters the code into a DataFrame
        resultsDF = pd.DataFrame.from_dict(df_new)
        # turns the json data to csv and gives each row an id
        resultsDF_CSV = resultsDF.to_csv(index=True)
        # write the content to the file
        f.write(resultsDF_CSV)