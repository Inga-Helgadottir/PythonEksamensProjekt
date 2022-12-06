from tkinter import *
import tkinter.font as font
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mtick

def statisticsPage(userName):
    from UI.ChooseCategoryPage import toChooseACategoryPage
    root = Tk()
    root.title("Hangman")
    root.iconbitmap("UI/HangmanIcon.ico")
    root.geometry("700x1000")
    root.configure(bg='black')

    ##############################colors################################
    # all the colors I will use
    green = "#00FF19"
    red = "#f00"
    blue = "#2C0AFF"
    white = "#fff"
    black = "#000"
    purpleHeaderBg = "#9B4AEC"

    ##############################variables################################
    myFontSize = 30

    ##############################frames################################
    headerFrame = LabelFrame(root, bg=purpleHeaderBg)
    headerFrame.pack()

    contentFrame = LabelFrame(root, bg=black, labelanchor=W+N, width=root.winfo_width(), borderwidth=0, highlightthickness=0)
    contentFrame.pack()

    headline = Label(headerFrame, text="Hangman", fg=white, bg=purpleHeaderBg, font=("Arial", 45), width=root.winfo_width())
    headline.pack(ipadx=2)

    ##############################text################################
    whatToDo = Label(contentFrame, text="What statistics would you like to see?", bg=black, fg=white, font=("Arial", myFontSize))
    whatToDo.grid(row=0, column=0, sticky=W+N+E+S, pady=5)
    
    ##############################button functions################################    
    def exitGame():
        root.destroy()      
    
    def barPlot():
        userCsvFile = "../EksamensProjekt/DataFiles/Users/" + userName + ".csv"
        userData = pd.read_csv(userCsvFile, usecols = ["guessWord", "wonOrLost", "category", "nbrOfGuesses", "hintsUsed"], encoding='latin-1')
        userData.plot(kind='bar',x='guessWord',y='nbrOfGuesses')
        plt.show()
    
    def groupByBarPlot():
        userCsvFile = "../EksamensProjekt/DataFiles/Users/" + userName + ".csv"
        userData = pd.read_csv(userCsvFile, usecols = ["guessWord", "wonOrLost", "category", "nbrOfGuesses", "hintsUsed"], encoding='latin-1')
        userData.groupby(["category","wonOrLost"]).size().groupby(level=0, group_keys=False).apply(lambda x: 100 * x / x.sum()).unstack().plot(kind='bar',stacked=True)
        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
        plt.show()

    def lineGraph():        
        userCsvFile = "../EksamensProjekt/DataFiles/Users/" + userName + ".csv"
        userData = pd.read_csv(userCsvFile, usecols = ["id", "wonOrLost", "category", "nbrOfGuesses", "hintsUsed"], encoding='latin-1')
        ax = plt.gca()
        userData.plot(kind='line',x='id',y='nbrOfGuesses',ax=ax)
        userData.plot(kind='line',x='id',y='hintsUsed', color='red', ax=ax)
        plt.show()

    def playAgain():
        root.destroy()  
        toChooseACategoryPage(userName)

    ##############################buttons################################
    exitButton = Button(contentFrame, text="Exit", command=exitGame, width=15, fg=white, bg=red, font=("Arial", myFontSize))
    exitButton.grid(row=5, column=0, sticky=W+N+S+E, ipadx=10, pady=25, padx=20)
    
    seeBarPlot = Button(contentFrame, text="See bar plot", command=barPlot, width=15, fg=white, bg=blue, font=("Arial", myFontSize))
    seeBarPlot.grid(row=1, column=0, sticky=W+N+S+E, ipadx=10, pady=25, padx=20)

    graphButton = Button(contentFrame, text="See line graph", command=lineGraph, width=15, fg=white, bg=blue, font=("Arial", myFontSize))
    graphButton.grid(row=2, column=0, sticky=W+N+S+E, ipadx=10, pady=25, padx=20)
    
    seegroupByBarPlot = Button(contentFrame, text="See group by bar plot", command=groupByBarPlot, width=15, fg=white, bg=blue, font=("Arial", myFontSize))
    seegroupByBarPlot.grid(row=3, column=0, sticky=W+N+S+E, ipadx=10, pady=25, padx=20)    
    
    playAgainButton = Button(contentFrame, text="Play game", command=playAgain, width=8, fg=black, bg=green, font=("Arial", myFontSize))
    playAgainButton.grid(row=4, column=0, sticky=W+N+S+E, ipadx=10, pady=25)

    root.mainloop()