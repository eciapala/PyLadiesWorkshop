#Zadanie dla chetnych

#wersja for
suma = 0
for ilosc_miesiecy in range(12):
    wynagrodzenie = int(input("Podaj wysokosc wynagrodzenia"))
    suma = suma + wynagrodzenie
srednia = suma / ilosc_miesiecy
print(srednia)

#wersja while
suma = 0
miesiac = 1
while (miesiac<13):
    wynagrodzenie = int(input("Podaj wartosc wynagrodzenia"))
    suma += wynagrodzenie
    miesiac += 1
print("Srednia: ", suma/12)
