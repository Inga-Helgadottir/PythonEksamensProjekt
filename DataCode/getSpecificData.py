import random
import csv

def getDataFromCategory(category):
    myMovieData = "../DataFiles/myMovieData.csv"
    myRickAndMortyData = "../DataFiles/myRickAndMortyData.csv"
    if category == "Movies":
        with open(myMovieData, 'r') as file_object:
            reader = csv.reader(file_object)
            chosenRow = random.choice(list(reader))
            print(chosenRow)
    else:
        with open(myRickAndMortyData, 'r') as file_object:
            reader = csv.reader(file_object)
            chosenRow = random.choice(list(reader))
            print(chosenRow)

getDataFromCategory("Movies")