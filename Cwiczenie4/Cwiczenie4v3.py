import re
#Wiktor Nosarzewski 15o3o24 Cwiczenie4 v3
#Program sprawdza czy user wprowadził prawidłowy kod pocztowy
#r przed stringiem oznacza przedrostek tekstu - string typu raw
#wzorzec = r"^\d[2]-\d[3]$" #pisownia kiedy się powtarza
#wzorzec = r"^\d\d-\d\d\d$" #kod pocztowy
while True:
    print("Wybierz opcję - wpisz numer od 0 do 6: \n")
    print("0. Sprawdz kod pocztowy")
    print("1. Dowolna liczba całkowita (dodatnia lub ujemna)")
    print("2. Dowolna liczba całkowita lub z częścią dziesiętną po kropce (dodatnia lub ujemna)")
    print("3. Występuje jeden lub więcej operatorów matematycznych")
    select = input("Wybierz działanie: ")
    if select == "0":
        wzorzec = r"^\d\d-\d\d\d$"
        tekst = input("Podaj kod pocztowy: ")
        wynik = re.search(wzorzec, tekst)
        if wynik is not None:
            #print("OK")
            print(f"Podany tekst '{tekst}' jest poprawnym kodem pocztowym.")
        else:
            #print("Zły format")
            print(f"Podany tekst '{tekst}' jest niepoprawny.")    
    if select == "1":
        wzorzec = r"-?\d+"
        tekst = input("Podaj: Dowolna liczba całkowita (dodatnia lub ujemna): ")
        wynik = re.search(wzorzec, tekst)
        if wynik is not None:
            #print("OK")
            print(f"Podany tekst '{tekst}' jest poprawny.")
        else:
            #print("Zły format")
            print(f"Podany tekst '{tekst}' jest niepoprawny.")
    if select == "2":
        wzorzec = r"-?\d+(\.\d+)?"
        tekst = input("Podaj: Dowolna liczba całkowita lub z częścią dziesiętną po kropce (dodatnia lub ujemna): ")
        wynik = re.search(wzorzec, tekst)
        if wynik is not None:
            #print("OK")
            print(f"Podany tekst '{tekst}' jest poprawny.")
        else:
            #print("Zły format")
            print(f"Podany tekst '{tekst}' jest niepoprawny.")        
    if select == "3":
        wzorzec = r"^\d+([\+\-\*\/]\d+)+$"
        tekst = input("Podaj: Dowolna liczba całkowita lub z częścią dziesiętną po kropce (dodatnia lub ujemna): ")
        wynik = re.search(wzorzec, tekst)
        if wynik is not None:
            #print("OK")
            print(f"Podany tekst '{tekst}' jest poprawny.")
        else:
            #print("Zły format")
            print(f"Podany tekst '{tekst}' jest niepoprawny.") 

