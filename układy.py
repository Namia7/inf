# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu arytmetycznego.

def genrate_text(file_name:str,content:str):
   file_name = file_name + ".txt"
   with open(file_name, "w") as text_file:
       text_file.write(content)


def cig_arytmetyczny(p_el,dr_el,n):
    el = p_el
    co_ile = dr_el - p_el
    text = f"{p_el} "
    for _ in range(n):
        text += f"{el+co_ile} "
        el += co_ile
    return text


text = cig_arytmetyczny(2,4,10)
genrate_text("ary", text)


# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu geometrycznego.

def genrate_text(file_name:str,content:str):
   file_name = file_name + ".txt"
   with open(file_name, "w") as text_file:
       text_file.write(content)


def cig_gem(p_el,dr_el,n):
    el = p_el
    co_ile = dr_el / p_el
    text = f"{p_el} "
    for _ in range(n):
        text += f"{el*co_ile} "
        el *= co_ile
    return text


text = cig_gem(5,10,10)
genrate_text("geom", text)    


# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu fibonacciego. 

def genrate_text(file_name:str,content:str):
  file_name = file_name + ".txt"
  with open(file_name, "w") as text_file:
      text_file.write(content)


def fibonacci_sequence(n):
   el_1 = 1
   el_2 = 1
   nex_el = 0
   text = f"{el_1} {el_2}"
   for _ in range(n):
       nex_el = el_1 + el_2
       text += f" {nex_el}"
       el_1 = el_2
       el_2 = nex_el
   return text


text = fibonacci_sequence(10)
genrate_text("fibo", text)