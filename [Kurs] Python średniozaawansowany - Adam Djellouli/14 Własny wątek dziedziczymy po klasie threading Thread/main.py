import threading
import time


class MojWatek(threading.Thread):
    def __init__(self, nazwa="Wątek", opoznienie=1, powtorzenia=3):
        threading.Thread.__init__(self)
        self.nazwa = nazwa
        self.opoznienie = opoznienie
        self.powtorzenia = powtorzenia

    def run(self):
        print(self.nazwa, "rozpoczyna działanie")
        for i in range(self.powtorzenia):
            print(self.nazwa, "idzie spać na", self.opoznienie, "sekund")
            time.sleep(self.opoznienie)
        print(self.nazwa, "kończy działanie")


print("Tworzymy dwa wątki")
watek1 = MojWatek("Wątek 1", 1, 8)
watek2 = MojWatek("Wątek 2", 2, 3)

watek1.start()
watek2.start()
watek1.join()
watek2.join()

print("Kończymy tę imprezę")
