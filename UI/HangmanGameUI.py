from tkinter import *
from PIL import ImageTk, Image
from getLines import showLines
import tkinter.font as font
from tkinter import ttk

def hangmanGamePage(categoryInfoText, spaceForLinesText, listOfGuessedText):
    root = Tk()
    root.title("Hangman")
    root.iconbitmap("../HangmanIcon.ico")
    root.geometry("1200x765")
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
    global hintNbr
    hintNbr = 0
    
    myWidth2 = 15
    myFontSize = 30
    hintFontSize = 15

    ##############################frames################################
    headerFrame = LabelFrame(root, bg=purpleHeaderBg)
    headerFrame.pack()

    contentFrame = LabelFrame(root, bg=black, labelanchor=W+N, width=root.winfo_screenwidth(), borderwidth=0, highlightthickness=0)
    contentFrame.pack()

    headline = Label(headerFrame, text="Hangman", fg=white, bg=purpleHeaderBg, font=("Arial", 45), width=root.winfo_width())
    headline.pack(ipadx=2)

    ##############################text################################
    categoryInfo = Label(contentFrame, text=categoryInfoText, bg=black, fg=white, font=("Arial", myFontSize))
    categoryInfo.grid(row=0, column=0, columnspan=2, sticky=W+N)

    spaceForLines = Label(contentFrame, text=spaceForLinesText, bg=black, fg=white, font=("Arial", myFontSize))
    spaceForLines.grid(row=1, column=0, sticky=W+N)

    listOfGuessed = Label(contentFrame, text=listOfGuessedText, bg=black, fg=white, font=("Arial", myFontSize))
    listOfGuessed.grid(row=2, column=0, columnspan=2, sticky=W+N, pady=20)
    
    hintText = Label(contentFrame, text="Hint: \nAction & Adventure, Comedy, Drama, Science Fiction & Fantasy", bg=green, fg=black, font=("Arial", hintFontSize))
    hintText.grid(row=5, column=51, columnspan=3, sticky=S+E+W+N, ipadx=10, pady=10)
    
    ##############################button functions################################    
    def exitGame():
        # add a function to save progress later
        root.quit()      

    def hintChecker():
        global hintNbr
        hintText.grid(row=5, column=0, columnspan=3, sticky=S+E+W+N, ipadx=10, pady=10)

        if hintNbr == 0:
            print("get first hint")
            hintNbr = 1
            return
        elif hintNbr == 1:
            print("get second hint")
            hintNbr = 2
            return
        elif hintNbr == 2:
            print("get third hint")
            hintNbr = 3
            hintButton.grid(row=50, column=50)
            return

    ##############################buttons################################
    exitButton = Button(contentFrame, text="Exit", command=exitGame, width=8, fg=white, bg=red, font=("Arial", myFontSize))
    exitButton.grid(row=4, column=0, sticky=S+W, ipadx=15, pady=5, padx=25)
    
    guessWordButton = Button(contentFrame, text="Guess a word", command=lambda: guessWord(), fg=white, bg=blue, width=myWidth2, font=("Arial", myFontSize))
    guessWordButton.grid(row=4, column=2, sticky=S+E, ipadx=15, pady=5, padx=25)

    hintButton = Button(contentFrame, text="Hint", command=hintChecker, fg=black, bg=green, font=("Arial", myFontSize))
    hintButton.grid(row=0, column=2, sticky=E+N, pady=5)

    guessSentenceButton = Button(contentFrame, text="Guess a sentence", command=lambda: guessSentence(), fg=white, bg=blue, width=myWidth2, font=("Arial", myFontSize))
    guessSentenceButton.grid(row=3, column=2, sticky=S+E, ipadx=15, pady=5, padx=25)

    ##############################inputs################################    
    guessSentenceInput = Entry(contentFrame, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2, font=("Arial", myFontSize))
    guessSentenceInput.grid(row=3, column=1, ipady=6, pady=11)

    guessWordInput = Entry(contentFrame, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2, font=("Arial", myFontSize))
    guessWordInput.grid(row=4, column=1, ipady=6, pady=11)
    
    ##############################image################################    
    hangmanImg = ImageTk.PhotoImage(Image.open("../HangmanFunctions/Images/start.jpg"))
    image = Label(contentFrame, image=hangmanImg)
    image.grid(row=2, column=2, sticky=W+N, pady=20)

    root.mainloop()
    
hangmanGamePage("Rick and Morty character", "_ _ _ _   _ _ _ _", "A, B")