number = 0

#while number < 10:
#    print("Nieskończoność...")
#    number += 1

count = 0

while count <= 100:
    if count % 50 == 0:
        count += 1
        continue
    if count % 20 == 0:
        break
    print("Nasze liczby: {}".format(count))
    count += 1

print("Koniec pętli")