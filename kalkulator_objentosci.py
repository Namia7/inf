from math import pi
def szescian_v (a):
    return a**3
while True:
    inp= input()
    if "f" ==inp:
        break
    elif "a"==inp:
        a = float(input())
        print(f"szescian_v={szescian_v(a)}")
    else:
        print("brak takiej opcji")


def prostopadloscian_v (a,b,c):
    return a*b*c
while True:
    inp= input()
    if "q" ==inp:
        break
    elif "b"==inp:
        a = float(input())
        b= float(input())
        c= float(input())
        print(f"prostopadloscian_v={prostopadloscian_v(a,b,c)}")
    else:
        print("brak takiej opcji")


def graniastoslup_v (Pp,H):
    return Pp*H
while True:
    inp= input()
    if "w" ==inp:
        break
    elif "c"==inp:
        Pp = float(input())
        H = float(input())
        print(f"graniastoslup_v={graniastoslup_v(Pp,H)}")
    else:
        print("brak takiej opcji")


def ostroslup_v (p,h):
    return 1/3*p*h
while True:
    inp= input()
    if "p" ==inp:
        break
    elif "d"==inp:
        p = float(input())
        h = float(input())
        print(f"ostroslup_v={ostroslup_v(p,h)}")
    else:
        print("brak takiej opcji")


def walc_v (r,n):
    return pi*r*r*n
while True:
    inp= input()
    if "v" ==inp:
        break
    elif "e"==inp:
        r = float(input())
        n = float(input())
        print(f"walc_v={walc_v(r,n)}")
    else:
        print("brak takiej opcji")


def stozek_v (t,m):
    return 1/3*pi*t*t*m
while True:
    inp= input()
    if "z" ==inp:
        break
    elif "g"==inp:
        t = float(input())
        m = float(input())
        print(f"stozek_v={stozek_v(t,m)}")
    else:
        print("brak takiej opcji")