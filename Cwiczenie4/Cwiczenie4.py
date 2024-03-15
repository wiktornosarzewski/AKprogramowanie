import re
#r przed stringiem oznacza przedrostek tekstu - string typu raw
wzorzec = r"\d\d-\d\d\d"
tekst = input("Podaj kod pocztowy: ")
wynik = re.search(wzorzec, tekst)
if wynik is not None:
    print("OK")
else:
    print("Zły format")
