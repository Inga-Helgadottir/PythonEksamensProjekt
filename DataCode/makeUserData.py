import pandas as pd
import numpy as np
import os

def makingAUser():
    userDataLocation = "../DataFiles/UserData.csv"
    userName = "start user1"
    password = "start pass"
    userNameStripped = userName.strip()
    userCsvFile = "../DataFiles/Users" + userNameStripped + ".csv"

    # check if there are any users in my user file
    if os.stat(userDataLocation).st_size == 0:
        # the file is empty so i need to add the column names
        writeThis = "userName, password, userCsvFile" + "\n" + str(userName) + ", " + str(password) + ", " + str(userCsvFile)
        with open(userDataLocation, "a", newline='') as f:
            f.write(writeThis)
    else:
        df = pd.read_csv(userDataLocation)

        checkingUserName = userName in df['userName'].values

        # file is not empty so i only need this users info
        writeThis = "\n" + str(userName) + ", " + str(password) + ", " + str(userCsvFile)

        if checkingUserName:
            return "User name already exists"
        else:
            with open(userDataLocation, "a", newline='') as f:
                f.write(writeThis)