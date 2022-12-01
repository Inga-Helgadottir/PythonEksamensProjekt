from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import ttk
from getLines import showLines

def chooseACategoryPage():#categoryInfoText, spaceForLinesText, listOfGuessedText, hintTexts):
    root = Tk()
    root.title("Hangman")
    root.iconbitmap("HangmanIcon.ico")
    root.geometry("900x600")
    root.configure(bg='black')

    ##############################colors################################
    # all the colors I will use
    green = "#00FF19"
    red = "#f00"
    blue = "#2C0AFF"
    white = "#fff"
    black = "#000"
    purpleHeaderBg = "#9B4AEC"
    purpleLogInAndSignInBg = "#6912C0"

    ##############################variables################################
    myWidth2 = 15
    myFontSize = 30
    hintFontSize = 15

    ##############################frames################################
    headerFrame = LabelFrame(root, bg=purpleHeaderBg)
    headerFrame.pack()

    contentFrame = LabelFrame(root, bg=black, labelanchor=W+N, width=root.winfo_width(), borderwidth=0, highlightthickness=0)
    contentFrame.pack()

    headline = Label(headerFrame, text="Hangman", fg=white, bg=purpleHeaderBg, font=("Arial", 45), width=root.winfo_width())
    headline.pack(ipadx=2)

    ##############################text################################
    category = Label(contentFrame, text="Choose a category", bg=black, fg=white, font=("Arial", myFontSize))
    category.grid(row=0, column=0, columnspan=3, sticky=W+N+E+S, pady=5)
    
    ##############################button functions################################    
    def exitGame():
        # add a function to save progress later
        root.quit()      

    ##############################buttons################################
    exitButton = Button(contentFrame, text="Exit", command=exitGame, width=8, fg=white, bg=red, font=("Arial", myFontSize))
    exitButton.grid(row=3, column=0, sticky=W+N+S+E, ipadx=10, pady=25)
    
    movieButton = Button(contentFrame, text="Movie names", command=lambda: movies(), fg=white, bg=blue, font=("Arial", myFontSize))
    movieButton.grid(row=1, column=0, sticky=W+N+S+E, ipadx=10, pady=25)

    RAMButton = Button(contentFrame, text="Rick and morty characters", command=lambda: ram(), fg=white, bg=blue, font=("Arial", myFontSize))
    RAMButton.grid(row=2, column=0, sticky=W+N+S+E, ipadx=10, pady=25)
    
    root.mainloop()