#by Wiktor Nosarzewski 23.02.2024r.
print("Przykładowe wartości: a = 1 b = 2 c = −3")
a = float(input("Podaj wartość parametru a: "))
b = float(input("Podaj wartość parametru b: "))
c = float(input("Podaj wartość parametru c: "))
delta = b**2 - 4*a*c

if delta < 0:
    print("Brak pierwiastków rzeczywistych.")
elif delta == 0:
    x = -b / (2*a)
    print(f"Jeden pierwiastek: x = {x}")
else:
    x1 = (-b - delta**0.5) / (2*a)
    x2 = (-b + delta**0.5) / (2*a)
    print(f"Dwa pierwiastki: x1 = {x1}, x2 = {x2}")
input("Wciśnij dowolny klawisz, aby zakończyć")
