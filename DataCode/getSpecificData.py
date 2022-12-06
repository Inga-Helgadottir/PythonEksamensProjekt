import pandas as pd

userCsvFileStart = "DataFiles/Users/"
usersCsvFile = "DataFiles/UserData.csv"

def getDataFromCategory(userName, category):
    myMovieData = "DataFiles/myMovieData.csv"
    myRickAndMortyData = "DataFiles/myRickAndMortyData.csv"
    userNameStripped = userName.strip()
    userCsvFile = userCsvFileStart + userNameStripped + ".csv"
    userData = pd.read_csv(userCsvFile, usecols = ["category", "guessWord"])

    if category == "Movies":
        movieData = pd.read_csv(myMovieData, encoding='latin-1')
        # add category data to the returned data
        movieData["category"] = "Movies"
        # putting together the data and deleting the duplicates
        mergedData = pd.merge(movieData,userData, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
        
        if len(mergedData) == 1:
            # if there is only one just return that line
            return mergedData
        else:
            # return a random row
            return mergedData.sample(n=1)
    else:
        ramcData = pd.read_csv(myRickAndMortyData, encoding='latin-1')
        # add category data to the returned data
        ramcData["category"] = "RAMC"
        # putting together the data and deleting the duplicates
        mergedData = pd.merge(ramcData,userData, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
        
        if len(mergedData) == 1:
            # if there is only one just return that line
            return mergedData
        else:
            # return a random row
            return mergedData.sample(n=1)
