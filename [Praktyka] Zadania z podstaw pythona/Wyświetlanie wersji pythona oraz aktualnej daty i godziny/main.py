import sys
from datetime import date
from datetime import datetime

# wyświetlanie aktualnej wersji Python
print("Current Python version: ", sys.version)
print("Version info: ", sys.version_info)

# wyświetlanie aktualnej daty i godziny
today = date.today()
now = datetime.now()
date = today.strftime("%d/%m/%y")
time = now.strftime("%H:%M:%S")

print("Current date:", date)
print("Current time", time)