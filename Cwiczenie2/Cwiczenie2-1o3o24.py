a = float(input("podaj a = "))
b = float(input("podaj b = "))
c = float(input("podaj c = "))
#By Wiktor Nosarzewski 1o3o24
print(f"Dane jest równanie {a} x^2 + {b}x + {c} - 0")
#np.4,5,1
delta = b*b - 4*a*c

if delta < 0:
    print("Równanie nie posiada rozwiązań")
    print(f"Delta = {delta}")
else:
    print("Obliczam pierwiastki")
    if delta == 0:
        x = -b / (2*a)
        #print(f"x = {x}")
        print(f"x = {x}")
    else:
        #x1 = (-b - math.sqrt(delta) / (2*a))
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta * 0.5) / (2*a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

print("Dziękujemy za użycie programu.")
                        
