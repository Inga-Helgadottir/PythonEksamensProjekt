from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from UI.ChooseCategoryPage import chooseACategoryPage

from UI.StatisticsPage import statisticsPage

def startOrStatistics(userName):
    root = Tk()
    root.title("Hangman")
    root.iconbitmap("UI/HangmanIcon.ico")
    root.geometry("900x600")
    root.configure(bg='black')

    ##############################colors################################
    # all the colors I will use
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
    whatToDo = Label(contentFrame, text="What do you want to do?", bg=black, fg=white, font=("Arial", myFontSize))
    whatToDo.grid(row=0, column=0, columnspan=3, sticky=W+N+E+S, pady=5)
    
    ##############################button functions################################    
    def exitGame():
        # add a function to save progress later
        root.destroy()      
    
    def statistics():
        root.destroy()
        statisticsPage(userName)

    def play():
        root.destroy()
        chooseACategoryPage(userName)

    ##############################buttons################################
    exitButton = Button(contentFrame, text="Exit", command=exitGame, width=15, fg=white, bg=red, font=("Arial", myFontSize))
    exitButton.grid(row=3, column=0, sticky=W+N+S+E, ipadx=10, pady=25, padx=20)
    
    seeStatistics = Button(contentFrame, text="See statistics", command=lambda: statistics(), width=15, fg=white, bg=blue, font=("Arial", myFontSize))
    seeStatistics.grid(row=1, column=0, sticky=W+N+S+E, ipadx=10, pady=25, padx=20)

    PlayTheGame = Button(contentFrame, text="Play the game", command=lambda: play(), width=15, fg=white, bg=blue, font=("Arial", myFontSize))
    PlayTheGame.grid(row=2, column=0, sticky=W+N+S+E, ipadx=10, pady=25, padx=20)
    
    root.mainloop()