liczby = [2,3,5,7]
for liczba in liczby:
    print(liczba)
print('\n')

licznik = 0
while licznik < 5:
     print(licznik)
     licznik += 1
print('\n')

for letter in 'Python':
    print ('Biezaca litera:', letter)
print('\n')

fruits = ['banan', 'jablko', 'gruszka']
for fruit in fruits:
    print ('Owoc:', fruit)
print('\n')

for num in range(10,20): #od 10 do 19
    print(num)
print('\n')

for num in range(10): #od 0 do 9
    print(num)
print('\n')

"""
#range
range(kiedy_stop)
for i in range(5):
    print(i) #0, 1, 2, 3, 4,
print('\n')

range(start, kiedy_stop)
for i in range(2,10):
    print(i) #2, 3, 4, 5, 6, 7, 8, 9
print('\n')


range(start, kiedy_stop, krok):
for i in range
    print(i)
print('\n')
"""

#petla for
moi_znajomi = ["Maciej Nowak", "Ania Kowalska", "Michu Bogacki", "Czarek Wieczorek", "Marta Kacprzak", "Staszek Piotrkowski", "Pawel Nowaczyk"]
for znajomy in range(5):
    nazwisko = input("Podaj nazwisko znajomego")
    moi_znajomi.append(nazwisko)
print(moi_znajomi)
