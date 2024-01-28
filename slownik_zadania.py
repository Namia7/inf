import funkcje_biblioteki

k: dict = {
    "nazwa": "Władca pierścieni",
    "liczbaStron": 300
}
k2: dict = {
    "nazwa": "Władca pierścieni",
    "liczbaStron": 300,
    "gatunek": "horror",
}

# bibliotek może być więcej
biblioteka: list[dict] = [k,k,k,k,k,k,k,k]
# biblioteka2 = [k,k,k,k,k,k,k,k]
# biblioteka3 = [k,k,k,k,k,k,k,k]



komendy = [
    "komendy",
    "informacje",
    "dodaj ksiazke",
    "edytuj ksiezke",
    "wyjdz",
]

while True:
    polecenie_bibliotekarza: str = input('Witamy w biblliotece, podaj komendę, lub wyświtl komendy wpisując "komendy" jako polecenie:')
    if polecenie_bibliotekarza == komendy[0]:
        for komenda in komendy:
            print('-', komenda)
    elif polecenie_bibliotekarza == komendy[1]:
        funkcje_biblioteki.opisz_informacje(biblioteka)
    elif polecenie_bibliotekarza == komendy[2]:
        nazwa_ksiazki: str = input("podaj nazwę książki: ")
        ilosc_stron: str = input("Podaj liczbe stron: ")
        k_: dict = {
            "nazwa": nazwa_ksiazki,
            "liczbaStron": int(ilosc_stron),  # int używamy żeby przerobić typ "łańcuch znaków" na "liczba całkowita", bo komputer to rozróżnia z człowiek już niekoniecznie 
        }
        biblioteka.append(k_)  # dodaj na koniec listy kolejną, nową książkę
    elif polecenie_bibliotekarza == komendy[3]:
        indeks_ksiazki: str = input("podaj ideks książki, którą chcesz zmienić: ")
        nowa_nazwa_ksiazki: str = input("podaj nazwę książki: ")
        nowa_ilosc_stron: str = input("Podaj liczbe stron: ")
        k_: dict = {
            "nazwa": nowa_nazwa_ksiazki,
            "liczbaStron": int(nowa_ilosc_stron),  
        }
        biblioteka[int(indeks_ksiazki)]=k_
    elif polecenie_bibliotekarza == komendy[-1]:
        print("Program zakończy działanie")
        break
    else:
        print(polecenie_bibliotekarza)
        print("Nie ma takiej komendy")