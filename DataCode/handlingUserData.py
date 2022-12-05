import pandas as pd
import numpy as np
import os
# import sys
# sys.path.append("..")
import random
from DataCode.getSpecificData import getDataFromCategory

userCsvFileStart = "../EksamensProjekt/DataFiles/Users/"
usersCsvFile = "../EksamensProjekt/DataFiles/UserData.csv"

def signUp(userName, password):
    userDataLocation = usersCsvFile
    userNameStripped = userName.strip()
    userCsvFile = userCsvFileStart + userNameStripped + ".csv"

    # if there are no users
    if os.stat(userDataLocation).st_size == 0:
        writeThis = "userName,password,userCsvFile" + "\n" + str(userName) + "," + str(password) + "," + str(userCsvFile)
        # add the column names and the first user
        with open(userDataLocation, "a", newline='') as f:
            f.write(writeThis)

        # make a csv file named after the users name with the column names
        writeThisInUserData = "category,guessWord,wonOrLost,correctGuesses,wrongGuesses,nbrOfGuesses,hintsUsed,gameCompleted\n"
        with open(userCsvFile, "w", newline='') as file:
            file.write(writeThisInUserData)
    else:
        df = pd.read_csv(userDataLocation)

        # find the username in the user file
        checkingUserName = userName in df['userName'].values

        # file is not empty so i only need this users info
        writeThis = "\n" + str(userName) + "," + str(password) + "," + str(userCsvFile)

        # if the user exists
        if checkingUserName:
            return "User name already exists"
        else:
            # add the user to the UserData.csv
            with open(userDataLocation, "a", newline='') as f:
                f.write(writeThis)
                
            # make a csv file named after the users name with the column names
            writeThisInUserData = "category,guessWord,wonOrLost,correctGuesses,wrongGuesses,nbrOfGuesses,hintsUsed,gameCompleted\n"
            with open(userCsvFile, "w", newline='') as file:
                file.write(writeThisInUserData)
            
            return "You are now logged in"

def logIn(userName, pasW):
    # print(pasW)
    userDataLocation = usersCsvFile
    df = pd.read_csv(userDataLocation)
    # checking if the username and password are correct  
    checkingUserAndPass = df.loc[(df['userName'] == userName) & (df['password'] == pasW) & (df['userCsvFile'] != "userCsvFile")]

    # check if the result is empty
    if checkingUserAndPass.empty:
        # the user with that password does not exist
        return False
    else:
        # the user name and password are correct
        return True

# returns the length of the users data (so I know if there is enough to show statistics)
def checkIfIShouldShowStatistics(userName):
    userNameStripped = userName.strip()
    userCsvFile = userCsvFileStart + userNameStripped + ".csv"
    userData = pd.read_csv(userCsvFile)
    return len(userData)

def saveUserGameInfo(userName, category, guessWord, wonOrLost, correctGuesses, wrongGuesses, nbrOfGuesses, hintsUsed, gameCompleted):
    userNameStripped = userName.strip()
    userCsvFile = userCsvFileStart + userNameStripped + ".csv"

    writeThis = str(category) + "," + str(guessWord) + "," + str(wonOrLost) + "," + str(correctGuesses) + "," + str(wrongGuesses) + "," + str(nbrOfGuesses) + "," + str(hintsUsed) + "," + str(gameCompleted) + "\n" 
    
    with open(userCsvFile, "a", newline='') as f:
        f.write(writeThis)

# makes random user data so I can test my statistics
def makeRandomUserData(userName, amountOfUserData):
    count = 0
    while count < amountOfUserData:
        getRAMC = getDataFromCategory(userName, "RAMC")
        getMovie = getDataFromCategory(userName, "Movies")
        
        if random.randint(0,1) == 1:
            wonOrLost = True
            guessWord = getRAMC.guessWord
            category = "RAMC"
        else: 
            wonOrLost = False
            guessWord = getMovie.guessWord
            category = "Movies"

        correctGuesses = "D_F_R_T_S_H"
        wrongGuesses = "P_S_R_E_W_X_WORD"
        nbrOfGuesses = random.randint(0,10)
        hintsUsed = random.randint(0,3)

        guessWordFix = str(guessWord.values.tolist())
        
        guessWordFix2 = guessWordFix.replace("'", "")
        guessWordFix3 = guessWordFix2.replace("[", "")
        guessWordFixed = guessWordFix3.replace("]", "")
       
        saveUserGameInfo(userName, category, guessWordFixed, wonOrLost, correctGuesses, wrongGuesses, nbrOfGuesses, hintsUsed, True)
        count = count + 1

# def getDataReadyForGame(userName, data):
