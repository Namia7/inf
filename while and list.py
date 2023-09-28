# 1
print("1-=-"*10)
numbers = []
print(len(numbers))

print(numbers)

# 2
i = 0
while i < 5:
    inp = float(input())
    numbers.append(inp)
    print(numbers)
    i += 1

# 3
numbers = [0,1,2,3,4,5,6,7,8,9,10]
print(numbers)



suma = 0
i = 0
while i < len(numbers):
    suma += numbers[i]
    i += 1
print(f"{numbers} - suma = {suma}")




# 4
print("4-=-"*10)
numbers = [0,1,2,3,4,5,6,7,8,9,10]


my_max = numbers[0]
i = 0
while i < len(numbers):
    if my_max < numbers[i]:
        my_max = numbers[i]
    i += 1
print(f"my_max = {my_max}")

# 5
print("5-=-"*10)
numbers = [0,1,2,3,4,5,6,7,8,9,10]


my_min = numbers[0]
i = 0
while i < len(numbers):
    if my_min > numbers[i]:
        my_min = numbers[i]
    i += 1
print(f"my_max = {my_min}")

# 6
print("6-=-"*10)
numbers = [0,1,2,3,4,5,6,7,8,9,10]
print(numbers)

my_sum = 0
i = 0
while i < len(numbers):
    my_sum += numbers[i]
    i += 1
print(my_sum/len(numbers))

# 7
print("7-=-"*10)
numbers = [0,1,2,3,4,5,6,7,8,9,10]


i = 0
parzyste = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
         parzyste += 1

# 8
numbers = [0,1,2,3,4,5,6,7,8,9,10,0,1,2,3,4,5,6,7,8,9,10]
duplicates = []
i = 0

while i < len(numbers):
    if numbers.count(numbers[i]) > 1 and numbers[i] not in duplicates:
        duplicates.append(numbers[i])
    i += 1
print(numbers)
print(duplicates)

# 9
print("9-=-"*10)
numbers = [1,1,1,2,2,5,5,5]
new_list = []


i = 0
while i < len(numbers):
    if numbers[i] not in new_list:
        new_list.append(numbers[i])
    i += 1

print(new_list)

# 10
print("9-=-"*10)
numbers = [1,1,1,2,2,5]
squares = []
i = 0
while i < len(numbers):
    squares.append(numbers[i]**2)
print(numbers)



# 2.1
liczba = float(input("Podaj liczbę: "))

if liczba > 0:
    print("Liczba jest dodatnia.")
elif liczba < 0:
    print("Liczba jest ujemna.")
else:
    print("Liczba jest równa zero.")

# 2.2
wiek = int(input("Podaj swój wiek: "))

if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    print("Jesteś niepełnoletni.")

# 2.3
n1 = float(input("Podaj pierwszą liczbę: "))
n2 = float(input("Podaj drugą liczbę: "))

if n1 > n2:
    print("Pierwsza liczba jest większa od drugiej.")
elif n1 < n2:
    print("Druga liczba jest większa od pierwszej.")
else:
    print("Obie liczby są równe.")

# 2.4
ocena = float(input("Podaj ocenę: "))

if ocena >= 4:
    print("Zaliczone.")
else:
    print("Niezaliczone.")

# 2.5
rok = int(input("Podaj rok: "))

if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print(rok, "jest rokiem przestępnym.")
else:
    print(rok, "nie jest rokiem przestępnym.")

# 2.6
liczba = int(input("Podaj liczbę: "))

if liczba % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

# 2.7
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

if a + b > c and b + c > a and c + a > b:
    print("Można zbudować trójkąt.")
else:
    print("Nie można zbudować trójkąta.")

# 2.8
liczba = int(input("Podaj liczbę: "))

if liczba % 3 == 0 and liczba % 5 == 0:
    print("Liczba jest podzielna przez 3 i 5.")
else:
    print("Liczba nie jest podzielna przez 3 i 5.")