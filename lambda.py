# Napisz funkcję która przyjmuje trzy listy i powie w której z nich znajduje się największa średnia.


def z_1(lst1, lst2, les3):
    sr = lambda lst: sum(lst)/len(lst)
    all_lst = [lst1,lst2,les3]
    w = []
    for lst in all_lst:
        w.append(sr(lst))
    return w.index(max(w))


print(z_1([1,2,3,4,5],[-2,-3,-6],[20]))


# Napisz funkcję która generuje losową listę o wielkości k i zakresie n i m.


from random import randint
z_2 = lambda k,n,m: [randint(n,m) for i in range(k)]
print(z_2(10,10,20))




# Napisz funkcję która przyjmuje listę i podniesie wszystkie elementy do kwadratu


z_3 = lambda lst: list(map(lambda el: el**2, lst))
print(z_3([2,3,4,5,6,7,8]))
 
# Napisz funkcję która przyjmuje listę i podniesie wszystkie elementy do 1/2


z_4 = lambda lst: list(map(lambda el: el**1/2, lst))
print(z_4([4,8,16]))



# Napisz funkcję która przyjmuje listę jako argument w zwróci ile występuje liczb parzystych  


z_5 = lambda lst: len(list(filter(lambda x: x % 2 == 0, lst)))
print(z_5([2,4,6]))
