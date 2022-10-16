txt = input()

listOfWordsInSentance = txt.split(" ")

numberOfWordsInInput = len(listOfWordsInSentance)
int(numberOfWordsInInput)

sortedWords = sorted(listOfWordsInSentance, key=len)
sortedWords.reverse()
print(sortedWords[0])