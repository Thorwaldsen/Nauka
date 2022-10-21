# Zadanie jest następujące. Przy użyciu języka Python, należy znaleźć najmniejszą oraz największa liczbę na liście.
sampleList = [1, 4, -4, 7, 8, 3]

def lowestNumber(listOfNumbers):
    lenght = len(listOfNumbers)
    highestValue = listOfNumbers[0]
    for i in range(lenght):
        if highestValue <= listOfNumbers[i]:
            highestValue = listOfNumbers[i]
            continue
        else:
            continue
    print("Highest number in the list:", highestValue)

def highestNumber(listOfNumbers):
    lenght = len(listOfNumbers)
    lowestValue = listOfNumbers[0]
    for i in range(lenght):
        if lowestValue >= listOfNumbers[i]:
            lowestValue = listOfNumbers[i]
            continue
        else:
            continue
    print("Lowest number in the list:", lowestValue)

lowestNumber(sampleList)
highestNumber(sampleList)