
import random
import string
from itertools import cycle


# Funkcja szyfrująca i dekodująca dane.
def crypt(c_input, master_key, c_mode):
    c_mk = [ord(ch) for ch in master_key]
    if c_mode == 'encrypt':
        c_input = [ord(ch) for ch in c_input]
        cycled = cycle(c_mk)
        c_output = [ch + next(cycled) for ch in c_input]
        return c_output
    elif c_mode == 'decrypt':
        c_input = [int(x) for x in c_input.split(',')]
        cycled = cycle(c_mk)
        c_output = [x if x >= 0 else 0 for x in [ch - next(cycled) for ch in c_input]]
        c_output = ''.join([chr(ch) for ch in c_output])
        return c_output
    else:
        pass


# Funkcja służąca do wyświetlania podglądu zapisanych danych.
def preview_records(master_key):

    # Otwarcie pliku i odczytanie danych.
    with open('vault.vt', 'r') as f:
        records = f.readlines()

    # Usunięcie z zakończeń linii znaku złamania linii '\n'.
    records = [record.strip('\n') for record in records]

    # Odszyfrowanie odczytanych danych.
    for i in range(len(records)):
        records[i] = ' '.join([
            crypt(records[i].split()[0], master_key=master_key,
                  c_mode='decrypt'),
            crypt(records[i].split()[1], master_key=master_key,
                  c_mode='decrypt'),
            crypt(records[i].split()[2], master_key=master_key,
                  c_mode='decrypt')
        ])

    # Wyświetlenie informacji dla użytkownika przy braku rekordów w pliku,
    if len(records) == 0:
        print("\nUnfortunately there are no passwords in the Vault.")
        return False

    # RYSOWANIE TABELI Z DANYMI
    # Określenie maksymalnych długości kolumn.
    id_max_width = len(max([str(len(records)), "ID"]))
    separator = ' '
    platform_max_width = len(
        max([r.split()[0] for r in records] + ["PLATFORM"], key=len))
    login_max_width = len(
        max([r.split()[1] for r in records] + ["LOGIN"], key=len))
    password_max_width = len(
        max([r.split()[2] for r in records] + ["PASSWORD"], key=len))

    # Wyświetlenie nagłówków kolumn.
    print("\n3. Preview stored passwords.")
    print("~" * (id_max_width + platform_max_width + login_max_width + password_max_width + 9))
    print("ID" + separator * (id_max_width - len("ID")), end=' | ')
    print("PLATFORM" + separator * (platform_max_width - len("PLATFORM")), end=' | ')
    print("LOGIN" + separator * (login_max_width - len("LOGIN")), end=' | ')
    print("PASSWORD" + separator * (password_max_width - len("PASSWORD")))

    # Osadzenie danych w tabeli.
    iterator = 1
    for r in records:
        id = str(iterator) + separator * (id_max_width - len(str(iterator))) + ' | '
        platform = r.split()[0] + separator * (
                    platform_max_width - len(r.split()[0])) + ' | '
        login = r.split()[1] + separator * (
                    platform_max_width - len(r.split()[1])) + ' | '
        password = r.split()[2] + separator * (
                    platform_max_width - len(r.split()[2]))

        line = id + platform + login + password
        print(line)
        iterator += 1

    print("~" * (id_max_width + platform_max_width + login_max_width + password_max_width + 9))


# Funkcja odpowiedzialna za zapisywanie danych podanych przez użytkownika
# do dedykowanego pliku vault.vt.
def store_password(master_key, password=None):
    # Łańcuchy znaków do użycia w funkcjach input.
    prompt = [
        "Platform -> ",
        "Login -> ",
        "Password -> ",
        "Repeat password -> "
    ]

    # Pobranie od użytkownika inputu.
    if password is None:
        print("\nProvide platform, login and password you want to store.")
        str_platform = ''.join(input(prompt[0]).split())
        str_login = ''.join(input(prompt[1]).split())
        password = ''.join(input(prompt[2]).split())
    else:
        print(f"\nProvide platform and login for the following password: {password}")
        str_platform = ''.join(input(prompt[0]).split())
        str_login = ''.join(input(prompt[1]).split())

    # Poddanie danych szyfrowaniu.
    encrypted = [
        ','.join([str(x) for x in
                  crypt(c_input=str_platform, master_key=master_key,
                        c_mode='encrypt')]),
        ','.join([str(x) for x in
                  crypt(c_input=str_login, master_key=master_key,
                        c_mode='encrypt')]),
        ','.join([str(x) for x in
                  crypt(c_input=password, master_key=master_key,
                        c_mode='encrypt')])
    ]

    # Połączenie zaszyfrowanych danych w jednolinijkowy rekord (łańcuch znaków).
    str_line = ' '.join(x for x in encrypted)

    # Zapisanie zaszyfrowanych danych do pliku.
    with open('vault.vt', 'a') as f:
        f.write(str_line + '\n')

    # Wyświetlenie informacji o pomyślnym zapisie dla użytkownika.
    print("Record was added to the Vault!")


# Funkcja sprawdzająca input użytkownika pod kątem tego, czy jest liczbą
# w określonym zakresie.
def input_as_digit(user_input, display_string, lower_thr, higher_thr):
    # Główna pętla funkcji działająca do momentu, aż użytkownik poda
    # oczekiwany przez aplikację input.
    while True:
        if user_input.isdigit():
            if lower_thr <= int(user_input) <= higher_thr:
                return int(user_input)
            else:
                print("Invalid input. Try again.")
                user_input = input(display_string)
                continue
        else:
            print("Invalid input. Try again.")
            user_input = input(display_string)
            continue


# Funkcja do generowania losowego hasła.
def generate_new_password(master_key):
    # Wyświetlenie informacji dla użytkownika.
    print(
        "\n1. Generate new password."
        "\nHow many numbers, letters and special characters\n"
        "you want to include in a generated password?"
    )

    # Łańcuchy znaków do użycia w funkcjach input.
    prompt = [
        "Numbers (from 0 to 10) -> ",
        "Letters (from 0 to 10) -> ",
        "Special characters (from 0 to 10) -> "
    ]

    # Główna pętla funkcji.
    while True:
        # Pobranie po kolei odpowiedzi użytkownika.
        # Do sprawdzania odpowiedzi użytkownika, czy jest liczbą i czy znajduje
        # się w przedziale od 0 do 10 służy funkcja input_as_digit.
        n_numbers = input_as_digit(user_input=input(prompt[0]),
                                   display_string=prompt[0], lower_thr=0,
                                   higher_thr=10)
        n_letters = input_as_digit(user_input=input(prompt[1]),
                                   display_string=prompt[1], lower_thr=0,
                                   higher_thr=10)
        n_special_chars = input_as_digit(user_input=input(prompt[2]),
                                         display_string=prompt[2], lower_thr=0,
                                         higher_thr=10)

        # Tworzenie ciągów losowych liczb, liter oraz znaków.
        str_numbers = ''.join([str(random.randint(0, 10)) for _ in range(n_numbers)])
        str_letters = ''.join([random.choice(string.ascii_letters) for _ in range(n_letters)])
        str_special_chars = ''.join([random.choice(string.punctuation) for _ in range(n_special_chars)])

        # Połączenie ze sobą utworzonych ciągów i wyrażenie ich w formie listy.
        password = list(str_numbers + str_letters + str_special_chars)
        random.shuffle(password)  # Przemieszanie elementów utworzonego hasła.

        # Połączenie ze sobą przemieszanych elementów do formy łańcucha znaków.
        password = ''.join(password)

        # Jeżeli użytkownik wybrał 0 liczb, 0 liter oraz 0 znaków, to program
        # domyślnie za hasło uznaje słowo None.
        if password == '':
            password = 'None'

        # Po wygenerowaniu hasła wyświetlić je dla użytkownika.
        print("\nGenerated password is:", password)

        # Zapytać się użytkownika co chce zrobić z hasłem dalej.
        print("What you want to do with it?")
        print(
            "1. Re-generate.\n"
            "2. Use it for storing a new record in the Vault.\n"
            "3. Discard and return to the main menu."
        )

        # Pobrać opcję podaną przez użytkownika.
        user_input = input_as_digit(input("(1/2/3) -> "), "(1/2/3) -> ", 1, 3)

        if user_input == 1:
            # Jeżeli użytkownik wybrał opcję nr 1, to ponowić iterację głównej
            # pętli while tej funkcji.
            print()
            continue
        elif user_input == 2:
            # Jeżeli użytkownik wybrał opcję nr 2, to wywołać funkcję do
            # przechowywania haseł i zakończyć działanie pętli while tej
            # funkcji.
            store_password(master_key, password)
            break
        else:
            # Jeżeli użytkownik wybrał opcję nr 3, to zakończyć działanie pętli
            # while tej funkcji, co spowoduje powrót do ciała funkcji
            # main_menu.
            break


# Funkcja wyświetlająca menu i sterująca częściowo aplikacją.
def main_menu(master_key):
    # Główna pętla funkcji. Działa do momentu zakończenia działania programu.
    while True:
        # Wyświetlenie menu głównego dla użytkownika.
        print(
            "\n------ Main Menu ------\n"
            "What you want to do?\n"
            "1. Generate new password.\n"
            "2. Store password.\n"
            "3. Preview stored passwords.\n"
            "4. Exit."
        )

        # Wybór opcji przez użytkownika.
        user_input = input("(1/2/3/4) -> ")

        if user_input == '1':
            # Wybór opcji nr 1: Przejście do generowania nowego hasła.
            generate_new_password(master_key)
            continue
        elif user_input == '2':
            # Wybór opcji nr 2: Przejście do dodawania istniejącego hasła.
            store_password(master_key)
            continue
        elif user_input == '3':
            # Wybór opcji nr 3: Podgląd przechowywany danych.
            preview_records(master_key)
            continue
        elif user_input == '4':
            # Wybór opcji nr 4: Zakończenie działania programu.
            print("\nYour passwords are veeery safe ;) Have a nice day!")
            exit()
        else:
            # Przy podaniu innej odpowiedzi użytkownik jest o tym informowany
            # i proszony o ponowienie udzielenia odpowiedzi. Pętla while
            # ponawia iterację.
            print("Invalid input. Try again.")


# Wyświetlenie nagłówka.
print(
    "\n~~~~~~~~~~~~~~~~~~~~~~~\n"
    "@@@@@    VAULT    @@@@@"
    "\n~~~~~~~~~~~~~~~~~~~~~~~"
)

# Przywitanie użytkownika.
print("\nGreetings Master! Please provide the Master Key to proceed!")

# Pobranie Klucza Mistrza (MK) od użytkownika.
master_key = input("Master Key -> ")

if master_key != '':
    # Jeżeli MK został podany, to wywołać funkcję main_menu.
    main_menu(master_key)
else:
    # Jeżeli MK nie został podany, to program kończy swoje działanie.
    print("No Key, no fun.")
