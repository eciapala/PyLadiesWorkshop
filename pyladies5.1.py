#Zad. 1
for num in range(0,27,2): #wypisz liczby parzyste
    print(num)
print('\n')

for i in range(27):
    if (i % 2 == 0):
        print(i)
print('\n')

#Zad. 2
moi_znajomi = ["Maciej Nowak", "Ania Kowalska", "Michu Bogacki", "Czarek Wieczorek", "Marta Kacprzak", "Staszek Piotrkowski", "Pawel Nowaczyk"]
for znajomy in moi_znajomi:
    print("Wesolych Swiat", znajomy)
print('\n')

#Zad. 3
ciag = "Ala ma 4 koty"
for znak in ciag:
    if znak.isdigit():
        print(znak)
print('\n')

#petla while
moi_znajomi = ["Maciej Nowak", "Ania Kowalska", "Michu Bogacki", "Czarek Wieczorek", "Marta Kacprzak", "Staszek Piotrkowski", "Pawel Nowaczyk"]
i = 0
while (i<5):
    nazwisko = input("Podaj nazwisko znajomego")
    moi_znajomi.append(nazwisko)
    i += 1
print(moi_znajomi)
