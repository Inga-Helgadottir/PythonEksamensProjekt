from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hangman")
root.iconbitmap("HangmanIcon.ico")

##############################colors################################
# all the colors I will use
green = "#00FF19"
red = "#f00"
blue = "#2C0AFF"
white = "#fff"
black = "#000"
purpleHeaderBg = "#9B4AEC"
purpleLogInAndSignInBg = "#6912C0"

##############################btns################################

# exitButton = Button(root, text="Exit", command=root.quit, fg=white, bg=red)
# exitButton.pack()

# signUpButton = Button(root, text="Sign up", command=lambda: signUp(), fg=black, bg=green)
# signUpButton.pack()

# logInButton = Button(root, text="Log in", command=lambda: logIn(), fg=black, bg=green)
# logInButton.pack()

# movieButton = Button(root, text="Movie names", command=lambda: movies(), fg=white, bg=blue)
# movieButton.pack()

# playTheGameButton = Button(root, text="Play the game", command=lambda: play(), fg=white, bg=blue)
# playTheGameButton.pack()

# seeStatisticsButton = Button(root, text="See statistics", command=lambda: seeStatistics(), fg=white, bg=blue)
# seeStatisticsButton.pack()

# RAMButton = Button(root, text="Rick and morty characters", command=lambda: ram(), fg=white, bg=blue)
# RAMButton.pack()

# hintButton = Button(root, text="Hint", command=lambda: hintChecker(), fg=black, bg=green)
# hintButton.pack()

# guessSentenceButton = Button(root, text="Guess a sentence", command=lambda: guessSentence(), fg=white, bg=blue)
# guessSentenceButton.pack()

# guessWordButton = Button(root, text="Guess a word", command=lambda: guessWord(), fg=white, bg=blue)
# guessWordButton.pack()

# playAgainButton = Button(root, text="Play again", command=lambda: playAgain(), fg=black, bg=green)
# playAgainButton.pack()

##############################inputs################################

# logInInputUN = Entry(root, width=50, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2)
# logInInputUN.pack(padx=10, pady=10)
# logInInputUN.insert(0, "User name")

# logInInputP = Entry(root, width=50, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2)
# logInInputP.pack(padx=10, pady=10)
# logInInputP.insert(0, "Password")

# signUpInputUN = Entry(root, width=50, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2)
# signUpInputUN.pack(padx=10, pady=10)
# signUpInputUN.insert(0, "User name")

# signUpInputP = Entry(root, width=50, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2)
# signUpInputP.pack(padx=10, pady=10)
# signUpInputP.insert(0, "Password")

# guessSentenceInput = Entry(root, width=50, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2)
# guessSentenceInput.pack(padx=10, pady=10)
# guessSentenceInput.insert(0, "")

# guessWordInput = Entry(root, width=50, bg=purpleLogInAndSignInBg, fg=white, borderwidth=2)
# guessWordInput.pack(padx=10, pady=10)
# guessWordInput.insert(0, "")

##############################labels################################
# headline = Label(root, text="Hangman")
# headline.pack()

# LogIn = Label(root, text="Log in")
# LogIn.pack()

# signUp = Label(root, text="Sign up")
# signUp.pack()

# userName = Label(root, text="User name")
# userName.pack()

# password = Label(root, text="Password")
# password.pack()

# chooseCategory = Label(root, text="Choose category")
# chooseCategory.pack()

# whatToDo = Label(root, text="What would you like to do?")
# whatToDo.pack()

# RAMCharacter = Label(root, text="Rick and Mory character")
# RAMCharacter.pack()

# MCharacter = Label(root, text="Movie name")
# MCharacter.pack()

# listOfGuessed = Label(root, text="add guessed later")
# listOfGuessed.pack()

# spaceForLines = Label(root, text="_ _ _ _   _ _ _ _")
# spaceForLines.pack()

# gameOverText = Label(root, text="Game over")
# gameOverText.pack()

# wonOrLostText = Label(root, text="You won!")
# wonOrLostText.pack()

# theAnswerWas = Label(root, text="The answer was something")
# theAnswerWas.pack()

# hintText = Label(root, text="Add hint later")
# hintText.pack()

root.mainloop()