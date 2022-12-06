from UI.HangmanGameUI import hangmanGamePage
from UI.getLines import showLines

def changeInfoForHangmanUI(user, toChange):
    guessWord = str(toChange["guessWord"].values[0]).strip()

    category = str(toChange["category"].values[0]).strip()

    if category == "RAMC":
        category = "Rick and Morty character"

    sentenceInfo = str(toChange["sentenceInfo"].values[0]).strip()
    lines = showLines(sentenceInfo)

    hints = []
    hintColumns = [col for col in toChange.columns if 'Hint' in col]

    for i in hintColumns:
        hintFix = str(toChange[i].values[0])
        hints.append(hintFix)

    hangmanGamePage(user, guessWord, category, lines, hints)

