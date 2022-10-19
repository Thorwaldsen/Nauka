#kod ma pobrać od wprowadzającego nazwę pliku wraz z rozszerzeniem, a następne wypisać jakie to rozszerzenie
userInput = input("Insert filename with extension: ")

fileNameSplited = userInput.split(".")
print("File extension is", fileNameSplited[1])