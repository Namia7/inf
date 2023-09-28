# 1
liczba = float(input("Podaj liczbę: "))


if liczba > 0:
    print("Liczba jest dodatnia.")
elif liczba < 0:
    print("Liczba jest ujemna.")
else:
    print("Liczba jest równa zero.")


# 2
    wiek = int(input("Podaj swój wiek: "))


if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    print("Jesteś niepełnoletni.")

# 3
n1 = float(input("Podaj pierwszą liczbę: "))
n2 = float(input("Podaj drugą liczbę: "))


if n1 > n2:
    print("Pierwsza liczba jest większa od drugiej.")
elif n1 < n2:
    print("Druga liczba jest większa od pierwszej.")
else:
    print("Obie liczby są równe.")

# 4
ocena = float(input("Podaj ocenę: "))


if ocena >= 4:
    print("Zaliczone.")
else:
    print("Niezaliczone.")

# 5
rok = int(input("Podaj rok: "))


if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print(rok, "jest rokiem przestępnym.")
else:
    print(rok, "nie jest rokiem przestępnym.")

# 6
liczba = int(input("Podaj liczbę: "))


if liczba % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

# 7
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))


if a + b > c and b + c > a and c + a > b:
    print("Można zbudować trójkąt.")
else:
    print("Nie można zbudować trójkąta.")

# 8
liczba = int(input("Podaj liczbę: "))


if liczba % 3 == 0 and liczba % 5 == 0:
    print("Liczba jest podzielna przez 3 i 5.")
else:
    print("Liczba nie jest podzielna przez 3 i 5.")