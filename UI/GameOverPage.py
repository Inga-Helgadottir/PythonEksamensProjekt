from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import ttk
from UI.ChooseCategoryPage import chooseACategoryPage

def hangmanGameOverPage(userName, winLooseText, theAnswerWasText):
    root = Tk()
    root.title("Hangman")
    root.iconbitmap("UI/HangmanIcon.ico")
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
    gameOver = Label(contentFrame, text="Game Over!", bg=black, fg=white, font=("Arial", myFontSize))
    gameOver.grid(row=0, column=0, columnspan=3, sticky=W+N+E+S, pady=5)
    
    # winLoose = Label(contentFrame, text=winLooseText, bg=black, fg=white, font=("Arial", myFontSize))
    winLoose = Label(contentFrame, text=winLooseText, bg=black, fg=white, font=("Arial", myFontSize))
    winLoose.grid(row=1, column=0, columnspan=3, sticky=W+N+E+S, pady=5)

    # theAnswer = Label(contentFrame, text=theAnswerText, bg=black, fg=white, font=("Arial", myFontSize))
    theAnswer = Label(contentFrame, text="The answer was: " + theAnswerWasText, bg=black, fg=white, font=("Arial", myFontSize))
    theAnswer.grid(row=2, column=0, columnspan=3, sticky=W+N+E+S, pady=5)

    
    ##############################button functions################################      
    def exitGame():
        root.destroy()    

    def playAgain():
        root.destroy()  
        chooseACategoryPage(userName)

    ##############################buttons################################
    exitButton = Button(contentFrame, text="Exit", command=exitGame, width=8, fg=white, bg=red, font=("Arial", myFontSize))
    exitButton.grid(row=4, column=0, sticky=S+W, ipadx=10, pady=25)
    
    playAgainButton = Button(contentFrame, text="Play again", command=playAgain, fg=black, bg=green, font=("Arial", myFontSize))
    playAgainButton.grid(row=3, column=0, sticky=W+S, pady=25)
    
    ##############################image################################    
    hangmanImg = ImageTk.PhotoImage(Image.open("../EksamensProjekt/HangmanFunctions/Images/step10.jpg"), master=contentFrame)
    image = Label(contentFrame, image=hangmanImg)
    image.grid(row=3, column=1, columnspan=2, rowspan=2, sticky=S+E+W+N, pady=20, padx=30)

    root.mainloop()