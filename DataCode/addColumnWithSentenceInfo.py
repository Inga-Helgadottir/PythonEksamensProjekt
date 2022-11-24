def makeSentenceInfo(sentence):
    # add !##! to the end of the word to make it easier to find out what the last char is
    sentence = sentence + "!##!"
    # split the sentence
    sentenceSplit = sentence.split(" ")
    # check is the last word
    check = sentenceSplit[-1]
    # endResult will get the code in the end EX: 2_5_4
    endResult = ""
    for i in sentenceSplit:
        # save the length of the current word
        lengthOfWord = len(i)
        # check if the current word is the last word
        if i == check:
            # if it is the last the n remove the last 4 characters "!##!"
            endResult = endResult + str(lengthOfWord - 4)        
        else:
            # else add _ after length of word
            endResult = endResult + str(lengthOfWord) + "_"
    return endResult
