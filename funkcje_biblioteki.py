# ----------------------------------------
def opisz_informacje(biblioteka_: list[dict]) -> None:
    '''funkcja wypissuje informacje o każdej książce lub pozycji w danej bibliotece'''
    for pozycja in biblioteka_:
        for klucz, wartosc in pozycja.items():
            print(f"{klucz} : {wartosc}")
        print("---"*10)  # odseparowane wizualnie
# ----------------------------------------