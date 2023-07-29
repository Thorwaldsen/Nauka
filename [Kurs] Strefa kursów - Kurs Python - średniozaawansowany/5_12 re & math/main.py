import glob
import os
import shutil
import json
import re

try :
    os.mkdir("./processed")
except OSError:
    print("./processed directory already exist")

recipts = [f for f in glob.glob(r".\processed\receipt-[0-9]*.json") if re.match(r".\processed\receipt-[0-9]*[2468]", f)]
subtotal = 0.0

for path in recipts:
    with open(path) as file:
        content = json.load(file)
        subtotal += float(content['value'])
    name = path.split("/")[-1]
    destination = r"C:\Users\Nauka\PycharmProjects\[Kurs] Strefa kursów - Kurs Python - średniozaawansowany\5_12 re & math\processed\{}".format(name)
    shutil.move(path, destination)
    print(f"File {path} moved to {destination}")
print("Receipt subtotal: $%.2f" % subtotal)