def showLines(sentenceInfo):
    lines = ""
    for i in sentenceInfo:
        if i == "_":
            lines = lines + "  "
        else:
            lines = lines + int(i) * "_ "
    return lines
