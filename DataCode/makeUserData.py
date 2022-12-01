import pandas as pd
import numpy as np
import os

def signUp(userName, password):
    userDataLocation = "../DataFiles/UserData.csv"
    userNameStripped = userName.strip()
    userCsvFile = "../DataFiles/Users/" + userNameStripped + ".csv"

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

def logIn(userName, pasW):
    # print(pasW)
    userDataLocation = "../DataFiles/UserData.csv"
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
        


# makeUserGameInfo("userName", "Movies", "guessWord", True, "E_D_F_Word", "S_R_O", 7, 1, False)
def makeUserGameInfo(userName, category, guessWord, wonOrLost, correctGuesses, wrongGuesses, nbrOfGuesses, hintsUsed, gameCompleted):
    userNameStripped = userName.strip()
    userCsvFile = "../DataFiles/Users/" + userNameStripped + ".csv"

    writeThis = str(category) + "," + str(guessWord) + "," + str(wonOrLost) + "," + str(correctGuesses) + "," + str(wrongGuesses) + "," + str(nbrOfGuesses) + "," + str(hintsUsed) + "," + str(gameCompleted) 
    
    with open(userCsvFile, "a", newline='') as f:
        f.write(writeThis)
