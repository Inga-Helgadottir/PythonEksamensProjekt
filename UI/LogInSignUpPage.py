from tkinter import *
from tkinter import messagebox 
from DataCode import handlingUserData
from DataCode.handlingUserData import checkIfIShouldShowStatistics
from UI.ChooseCategoryPage import toChooseACategoryPage
from UI.StartGameOrStatistics import startOrStatistics

def loginSignUpPage():
    root = Tk()
    root.title("Hangman")
    root.iconbitmap("UI/HangmanIcon.ico")
    root.geometry("800x700")
    root.configure(bg='black')

    ##############################colors################################
    # all the colors I will use
    green = "#00FF19"
    red = "#f00"
    white = "#fff"
    black = "#000"
    purpleHeaderBg = "#9B4AEC"
    purpleLogInAndSignInBg = "#6912C0"

    ##############################variables################################
    global hintNbr
    hintNbr = 0
    
    myFontSize = 30
    myLittleFontSize = 15

    ##############################frames################################
    headerFrame = LabelFrame(root, bg=purpleHeaderBg)
    headerFrame.pack()

    logInFrame = LabelFrame(root, bg=purpleLogInAndSignInBg, labelanchor=W+N, width=root.winfo_width(), borderwidth=0, highlightthickness=2)
    logInFrame.pack(padx=5, pady=5, ipady=10)

    signUpFrame = LabelFrame(root, bg=purpleLogInAndSignInBg, labelanchor=W+N, width=root.winfo_width(), borderwidth=0, highlightthickness=2)
    signUpFrame.pack(padx=5, pady=5, ipady=10)

    contentFrame = LabelFrame(root, bg=black, labelanchor=W+N, width=root.winfo_width(), borderwidth=0, highlightthickness=0)
    contentFrame.pack()

    ##############################text################################
    headline = Label(headerFrame, text="Hangman", fg=white, bg=purpleHeaderBg, font=("Arial", 45), width=root.winfo_width())
    headline.pack(ipadx=2)

    logIn = Label(logInFrame, text="Log in", fg=white, bg=purpleLogInAndSignInBg, font=("Arial", myFontSize))
    logIn.grid(row=0, column=0, columnspan=2, sticky=W+E+S+N, pady=10)

    lIUserName = Label(logInFrame, text="User name", fg=white, bg=purpleLogInAndSignInBg, font=("Arial", myLittleFontSize))
    lIUserName.grid(row=1, column=0, sticky=W+N, pady=10)

    lIPassword = Label(logInFrame, text="Password", fg=white, bg=purpleLogInAndSignInBg, font=("Arial", myLittleFontSize))
    lIPassword.grid(row=2, column=0, sticky=W+N, pady=10)

    signUp = Label(signUpFrame, text="Sign up", fg=white, bg=purpleLogInAndSignInBg, font=("Arial", myFontSize))
    signUp.grid(row=0, column=0, columnspan=2, sticky=W+E+S+N, pady=10)

    sUUserName = Label(signUpFrame, text="User name", fg=white, bg=purpleLogInAndSignInBg, font=("Arial", myLittleFontSize))
    sUUserName.grid(row=1, column=0, sticky=W+N, pady=10)

    sUPassword = Label(signUpFrame, text="Password", fg=white, bg=purpleLogInAndSignInBg, font=("Arial", myLittleFontSize))
    sUPassword.grid(row=2, column=0, sticky=W+N, pady=10)
    
    ##############################button functions################################    
    def exitGame():
        # add a function to save progress later
        root.quit()    

    def logInFunc(userName, password):
        checkLogin = handlingUserData.logIn(userName, password)
        if checkLogin:
            showStatistics = checkIfIShouldShowStatistics(userName)
            if showStatistics > 4:
                root.destroy()
                startOrStatistics(userName)
            else:
                root.destroy()
                toChooseACategoryPage(userName)
        else:
            messagebox.showerror("Input error", "The user name or password is wrong")

    def signUpFunc(userName, password):
        if len(userName) == 0 or len(password) == 0:
            messagebox.showerror("Input error", "Please enter a user name and password")
        else:
            checkSignUp = handlingUserData.signUp(userName, password)
            if checkSignUp == "You are now logged in":
                root.destroy()
                toChooseACategoryPage(userName)
            else:
                messagebox.showerror("Input error", "The user name you have entered is already taken")

                

    ##############################buttons################################
    exitButton = Button(contentFrame, text="Exit", command=exitGame, width=8, fg=white, bg=red, font=("Arial", myFontSize))
    exitButton.grid(row=4, column=0, sticky=S+W, ipadx=15, pady=5, padx=25)
    
    signUpButton = Button(signUpFrame, text="Sign up", command=lambda: signUpFunc(signUpInputUN.get(), signUpInputP.get()), width=5, fg=black, bg=green, font=("Arial", 20))
    signUpButton.grid(row=3, column=0, columnspan=2, padx=30, sticky=W+E+S+N)

    logInButton = Button(logInFrame, text="Log in", command=lambda: logInFunc(logInInputUN.get(), logInInputP.get()), width=5, fg=black, bg=green, font=("Arial", 20))
    logInButton.grid(row=3, column=0, columnspan=2, padx=30, sticky=W+E+S+N)

    ##############################inputs################################    

    logInInputUN = Entry(logInFrame, width=20, bg=purpleHeaderBg, fg=white, borderwidth=2, font=("Arial", myLittleFontSize), highlightthickness=1)
    logInInputUN.grid(row=1, column=1, padx=10, pady=10, sticky=E)
    logInInputUN.insert(0, "")

    logInInputP = Entry(logInFrame, width=20, bg=purpleHeaderBg, fg=white, borderwidth=2, font=("Arial", myLittleFontSize), highlightthickness=1)
    logInInputP.grid(row=2, column=1, padx=10, pady=10, sticky=E)
    logInInputP.insert(0, "")

    signUpInputUN = Entry(signUpFrame, width=20, bg=purpleHeaderBg, fg=white, borderwidth=2, font=("Arial", myLittleFontSize), highlightthickness=1)
    signUpInputUN.grid(row=1, column=1, padx=10, pady=10, sticky=E)
    signUpInputUN.insert(0, "")

    signUpInputP = Entry(signUpFrame, width=20, bg=purpleHeaderBg, fg=white, borderwidth=2, font=("Arial", myLittleFontSize), highlightthickness=1)
    signUpInputP.grid(row=2, column=1, padx=10, pady=10, sticky=E)
    signUpInputP.insert(0, "")

    root.mainloop()