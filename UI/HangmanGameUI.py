from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import ttk
from UI.getLines import showLines
from tkinter import messagebox
import os
from os import listdir

def hangmanGamePage(userName, guessWord, categoryInfoText, linesText, listOfGuessedText, hintTexts):
    root = Tk()
    root.title("Hangman")
    root.iconbitmap("UI/HangmanIcon.ico")
    root.geometry("1200x800")
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

    global currentHintText
    currentHintText = ""

    global hangmanImages
    hangmanImages = []
    
    folder_dir = "../EksamensProjekt/HangmanFunctions/Images/"
    for images in os.listdir(folder_dir):
        if (images.endswith(".jpg")):
            hangmanImages.append(images)

    # making sure that step10 is last
    myorder = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 2]
    hangmanImages = [hangmanImages[i] for i in myorder]    

    global currentHangmanImg
    currentHangmanImg = "../EksamensProjekt/HangmanFunctions/Images/" + hangmanImages[0]

    global correctGuesses
    correctGuesses = []

    global wrongGuesses
    wrongGuesses = []

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
    categoryInfo = Label(contentFrame, text=categoryInfoText, bg=black, fg=white, font=("Arial", myFontSize))
    categoryInfo.grid(row=0, column=0, columnspan=2, sticky=W+N)

    spaceForLines = Label(contentFrame, text=linesText, bg=black, fg=white, font=("Arial", myFontSize))
    spaceForLines.grid(row=1, column=0, columnspan=2, sticky=W+N)

    listOfGuessed = Label(contentFrame, text=listOfGuessedText, bg=black, fg=white, font=("Arial", myFontSize))
    listOfGuessed.grid(row=2, column=0, columnspan=2, sticky=W+N, pady=20)
    
    hintText = Label(contentFrame, text=currentHintText, bg=green, fg=black, font=("Arial", hintFontSize))
    
    ##############################button functions################################    
    def exitGame():
        # add a function to save progress later
        root.quit()      

    def hintChecker():
        global hintNbr
        
        if hintNbr == 0:
            if categoryInfoText == "Movies":
                currentHintText = "This movies genre is " + hintTexts[0]
            else: 
                currentHintText = "This persons species is " + hintTexts[0]
            # move the hint text so you can see it on the screen
            hintText = Label(contentFrame, text=currentHintText, bg=green, fg=black, font=("Arial", hintFontSize))
            hintText.grid(row=5, column=0, columnspan=3, sticky=S+E+W+N, ipadx=10, pady=8)
            hintNbr = 1
            return
        elif hintNbr == 1:
            if categoryInfoText == "Movies":
                currentHintText = "This movies director is " + hintTexts[1]
            else: 
                currentHintText = "This persons gender is " + hintTexts[1]
            # add the hint text so you can see it on the screen
            hintText = Label(contentFrame, text=currentHintText, bg=green, fg=black, font=("Arial", hintFontSize))
            hintText.grid(row=6, column=0, columnspan=3, sticky=S+E+W+N, ipadx=10, pady=8)
            hintNbr = 2
            return
        elif hintNbr == 2:
            if categoryInfoText == "Movies":
                currentHintText = "This movies studio is " + hintTexts[2]
            else: 
                currentHintText = "This persons origin is " + hintTexts[2]
            # add the hint text so you can see it on the screen
            hintText = Label(contentFrame, text=currentHintText, bg=green, fg=black, font=("Arial", hintFontSize))
            hintText.grid(row=7, column=0, columnspan=3, sticky=S+E+W+N, ipadx=10, pady=8)
            hintNbr = 3
            # disables the hint button
            hintButton = Button(contentFrame, text="Hint", fg=black, bg="#727375", font=("Arial", myFontSize), state=DISABLED)
            hintButton.grid(row=0, column=2, sticky=E+N, pady=5)            
            return

    def handleGuess(guess):
        # guessWord, categoryInfoText, LinesText, listOfGuessedText, hintTexts
        guessCheck = guessWord.upper().strip()
        currentGuessUpper = guess.upper().strip()
        if len(guess) == 0:
            messagebox.showerror("Input error", "The input is empty")
        elif len(guess) == 1:
            # for i in guessWord:

            return "CHECK AGAINST GUESS WORD"
        else:
            if guessCheck == currentGuessUpper:
                print("yes")
                # you won the game
                    # save info to personal user data
            else:
                print("no")
                # wrongGuesses.append(guess)
        # lists of guesses:
            # correctGuesses.append(guess)
            # wrongGuesses.append(guess)

        # def gameOver(wonOrLost):
        #     if wonOrLost == "Won":
        #         S
        #     else:


    ##############################buttons################################
    exitButton = Button(contentFrame, text="Exit", command=exitGame, width=8, fg=white, bg=red, font=("Arial", myFontSize))
    exitButton.grid(row=3, column=0, sticky=S+W, ipadx=15, pady=5, padx=25)

    hintButton = Button(contentFrame, text="Hint", command=hintChecker, fg=black, bg=green, font=("Arial", myFontSize))
    hintButton.grid(row=0, column=2, sticky=E+N, pady=5)

    guessSentenceButton = Button(contentFrame, text="Guess", command=lambda: handleGuess(guessSentenceInput.get()), fg=white, bg=blue, width=myWidth2, font=("Arial", myFontSize))
    guessSentenceButton.grid(row=3, column=2, sticky=S+E, ipadx=15, pady=5, padx=25)

    ##############################inputs################################    
    guessSentenceInput = Entry(contentFrame, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2, font=("Arial", myFontSize))
    guessSentenceInput.grid(row=3, column=1, ipady=6, pady=11)
    
    ##############################image################################  
    hangmanImg = ImageTk.PhotoImage(Image.open(currentHangmanImg), master=contentFrame)
    image = Label(contentFrame, image=hangmanImg)
    image.grid(row=2, column=2, sticky=W+N, pady=20)

    root.mainloop()