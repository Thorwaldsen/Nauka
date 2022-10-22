# program posiada listę liczb.  Należy posortować ją rosnąco, za pomocą algorytmu bąbelkowego

listOfNumbers = [2, 1, 3, 7, 8, 3, 7, 9]
numberOfElements = len(listOfNumbers)
count = 0
temp = 0
swapped = True

print("Unsorted:", listOfNumbers)

while swapped:
    swapped = False
    for unsorted in range(numberOfElements - 1 - temp):
        count += 1
        if listOfNumbers[unsorted] > listOfNumbers[unsorted + 1]:
            listOfNumbers[unsorted], listOfNumbers[unsorted + 1] = listOfNumbers[unsorted + 1], listOfNumbers[unsorted]
            swapped = True
    temp += 1

print("Number of iterations:", count)
print("Sorted:", listOfNumbers)
