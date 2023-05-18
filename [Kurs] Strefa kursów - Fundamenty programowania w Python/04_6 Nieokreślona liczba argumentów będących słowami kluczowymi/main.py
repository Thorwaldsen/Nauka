def wyswietl_stolicę(**kwargs):
    panstwa_miasta = kwargs
    print(panstwa_miasta, type(panstwa_miasta))
    for panstwo, stolica in panstwa_miasta.items():
        print(f"Stolicą państwa {panstwo} jest miasto {stolica}.")


wyswietl_stolicę(
    Polska="Warszawa",
    Ukraina="Kijów",
    Finlandia="Helsinki",
    Norwegia="Oslo",
    Mołdawia="Kiszyniów"
)
