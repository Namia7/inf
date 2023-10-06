# import random

# lst = []
# while len(lst) != 20:
#     rnd = random.randint(100,200)
#     if rnd % 5 != 0:
#         lst.append(rnd)
# print(lst)



# inp = input()
# d_ile =0
# v_ile =0
# b_ile =0
# n_ile =0
# k_ile =0
# for el in inp:
#     if el == 'd':
#         d_ile +=1
#     if el == 'v':
#         v_ile +=1
#     if el == 'b':
#         b_ile +=1
#     if el == 'n':
#         n_ile +=1
#     if el == 'k':
#         k_ile +=1
# print(f"d --- {d_ile} v --- {v_ile} b --- {b_ile} n --- {n_ile} k --- {k_ile}")

# from random import randint
# lista = [randint(-10,10) for el in range(100)]
# print(lista)

# mniejsze_od_0 =0
# for el in lista:
#     if el  < 0:
#         mniejsze_od_0 += 1
# print(mniejsze_od_0)

# print(len(lista - mniejsze_od_0)

# wieksze_lub_0 =0
# for el in lista:
#     if el  < 0:
#         wieksze_lub_0 += 1
# print(wieksze_lub_0)




# xxx =0
# for el in lista:
#     if el % 2!= 0:
#         xxx ==el
# print(xxx)


# xxx=0
# for el in lista:
#     if el % 2!= 0:
#         xxx ==el
# print(xxx)


from random import randint
listy = [5,10,15,20,25,30,35,40,45,50]
print(listy)

suma = 0
i = 0
while i < len(listy):
    suma += listy[i]
    i += 1
print(f"{listy} - suma = {suma}")