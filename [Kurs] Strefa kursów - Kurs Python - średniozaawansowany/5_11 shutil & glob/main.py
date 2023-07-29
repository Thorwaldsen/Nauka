import glob
import os
import shutil
import json

try :
    os.mkdir("./processed")
except OSError:
    print("./processed directory already exist")

recipts = glob.glob(r'C:\Users\Nauka\PycharmProjects\[Kurs] Strefa kursów - Kurs Python - średniozaawansowany\5_11 shutil & glob\receipts\receipt-[0-9]*.json')
subtotal = 0.0

for path in recipts:
    with open(path) as file:
        content = json.load(file)
        subtotal += float(content['value'])
    name = path.split("/")[-1]
    destination = r"C:\Users\Nauka\PycharmProjects\[Kurs] Strefa kursów - Kurs Python - średniozaawansowany\5_11 shutil & glob\processed\{}".format(name)
    shutil.move(path, destination)
    print(f"File {path} moved to {destination}")
print("Receipt subtotal: $%.2f" % subtotal)
