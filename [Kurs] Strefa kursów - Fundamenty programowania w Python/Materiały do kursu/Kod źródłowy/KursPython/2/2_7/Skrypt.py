# PRZYKŁADY SŁOWNIKÓW
x = {}  # Pusty słownik
x = dict()  # J/w
x = {"Nazwisko": "Mikiciuk", "Wiek": 40}  # Słownik z dwoma parami klucz-wartość
x = dict([("Nazwisko", "Mikiciuk"), ("Wiek", 40)])  # J/w
x = dict(Nazwisko="Mikiciuk", Wiek=40)  # J/w

# POBIERANIE WARTOŚCI ZE SŁOWNIKA
nazwisko = x["Nazwisko"]
wiek = x.get("Wiek")

# Jeżeli podany klucz nie istnieje, to zostanie zwrócony łańcuch "Ten klucz nie istnieje!"
stanowisko = x.get("Stanowisko", "Ten klucz nie istnieje!")

# DODAWANIE PAR KLUCZ-WARTOŚĆ
x["Stanowisko"] = "Król Życia"  # Dodanie nowej pary klucz-wartość
nowe_pary = {"Wzrost": 190.0, "Waga": 90.0}
x.update(nowe_pary)  # Dodawanie wielu par klucz-wartość na raz (do słownika 'x')

# MODYFIKOWANIE WARTOŚCI
x["Wiek"] = 35  # Modyfikacja wartości w jednej z par klucz-wartość
aktualizacja_par = {"Stanowisko": "Imperator Drogi Mlecznej", "Wiek": 25}
x.update(aktualizacja_par)  # Aktualizacja wielu wartości na raz.

# USUWANIE PAR KLUCZ-WARTOŚĆ
pobrane_nazwisko = x.pop("Nazwisko")  # Usunięcie pary klucz-wartość z pobraniem wartości

# Jeżeli podany klucz nie istnieje, to zostanie zwrócony łańcuch "Nie ma takiego klucza!"
nie_ma_takiego_klucza = x.pop("Dochód", "Nie ma takiego klucza!")
del x["Wiek"]  # Usunięcie pary klucz-wartość
x.clear()  # Usunięcie wszystkich par klucz-wartość

# WYBRANE METODY
x = {1: 'a', 2: 'b', 3: 'c'}
klucze = x.keys()  # Pobranie kluczy
wartosci = x.values()  # Pobranie wartości
pary = x.items()  # Pobranie par klucz-wartość
