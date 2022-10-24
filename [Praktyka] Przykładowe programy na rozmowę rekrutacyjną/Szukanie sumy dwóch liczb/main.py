# program posiada listę, która zawiera cyfry. Kod ma przyjąć od użytkownika cyfrę, a następnie sprawdzić czy
# podana cyfra to to suma dowolnych dwóch elementów z listy. Czyli przykładowo, mamy podaną listę A = [1,3,5,2,11,7] .
# Należy sprawdzić czy suma, którychkolwiek liczb na liście wynosi 9.

listOfNumbers = [1, 3, 5, 2, 9, 7]
listLenght = len(listOfNumbers)
searched = input("Number: ")
searchedInt = int(searched)
found = True

def sumOfTwo(lenghtOfList, numbersList, searchedInput):
    for outerLoop in range(lenghtOfList):
        for innerLoop in range(outerLoop + 1, lenghtOfList):
            if numbersList[outerLoop] + numbersList[innerLoop] == searchedInput:
                print("Numbers found: ", numbersList[outerLoop]," + ", numbersList[innerLoop], " = ", searchedInput)

sumOfTwo(listLenght, listOfNumbers, searchedInt)