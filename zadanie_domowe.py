from datetime import datetime

PLIK_TEKSTOWY = "forum_internetowe.txt"


def wyswietl_posty():
    """wyświetla wszystkie posty z pliku"""
    with open(PLIK_TEKSTOWY, "r") as plik_forum:
        for linijka in plik_forum:  # wyświetl plik linijka po linijce

            print(linijka[:-1])  # omin ostatni znak, który tutaj będzie "\n"
            # bo i tak wyświetlany linijka po linijce więc po co dublować


def zapisz_post(tresc: str, autor: str):
    """dopisz post do pliku forum"""
    # uzyskaj datę posta, ale usuń mikrosekundy po kropce (":-7]") czyli do 7 znaku od końca
    data_posta = str(datetime.now())[:-7]
    post_do_dodania = f"   autor: {autor}\n   data:  {data_posta}\n{tresc}"

    with open(PLIK_TEKSTOWY, "a") as plik_forum:
        # dodaj posta z odstępem przed i po poście dla widoczności
        plik_forum.write("\n" + post_do_dodania + "\n")


def jak_dziala_join_przy_tekscie():
    """wyjaśnienie jak działa " ".join() i jakie argumenty przyjmuje"""
    # prezentacja jak domyslnie dziala print()
    print("ala ma kota")
    # domyslnie skleja argumenty po przecinkach przy pomocy spacji " "
    print("ala", "ma", "kota", "kota", "kota", "kota")
    # czyli powyższe będzie wyświetlone jako "ala ma kota kota kota kota"


    # poniżej -> sklej spacją (" ") argumenty podane w liście elementów
    lista_argumentow = ["ala", "ma", "kota", "kota", "kota", "kota"]
    print(" ".join(lista_argumentow))  # "ala ma kota kota kota kota"
    # czyli w sumie tak samo jak zwykły print("ala", "ma", "kota", "kota", "kota", "kota")

    # sklej używając ", ale " jako to czym sklejamy
    print(", ale ".join(lista_argumentow))  # "ala, ale ma, ale kota, ale kota, ale kota, ale kota"

    # sklej używając "\n", czli "znak specjalny nowej linii" jako to czym sklejamy
    print("\n".join(lista_argumentow))
    # sklej po prostu elementy ze sobą
    print("".join(lista_argumentow))  # "alamakotakotakotakota"

    # w ten sposób można rozwiązać problem wyświetlania postów:
    # print( "".join(plik_forum.readlines()) )


if __name__ == '__main__':
    zapisz_post("jestem super programistką Pythona!", "Natalia")
    wyswietl_posty()
