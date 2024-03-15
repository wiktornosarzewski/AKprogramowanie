#Cwiczenie 4.2 15o3o24 Wiktor Nosarzewski
import re #regex
tekst = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
regex = r"\."
#regex = r"[\.\,]"
lista = re.split(regex, tekst) #separacja tekstu
print(lista[1])
print("Następne: \n")
regex = r"[\.\,]"
lista = re.split(regex, tekst) #separacja tekstu
print(lista[1])
#znajdz i zamien
#regex1 = r"\s"
regex1 = r"\s+"
regex2 = r"\n"
tekst2 = re.sub(regex1,regex2,tekst)
tekst3 = re.sub("[\D\S]", "", tekst2)
print(tekst2)
print("Następne: \n")
print(tekst3)
#znajdz wszystkie {tyle znakow}: znajdz wszystkie słowa 4-literowe
#regex3 = "\b[A-Za-z]{2}\b"
regex3 = "\b[A-Za-z]{4}\b"
lista = re.findall(regex3,tekst)
print(lista)
