
"""
filmy = ["Titanic", "Dirty Dancing", "Krol Lew", "Spiaca Krolewna", "Iniemamocni", "Spiderman", "Britanic", "Swieta Wojna"]

print filmy[0]
print filmy[6]
print filmy[7]
print filmy[:4]
print filmy[4:] lub [-4:0]
print filmy[3:7]


film_5 = filmy[4]
litera_3 = film_5[2]

moi_znajomi = ["Maciej Nowak", "Ania Kowalska", "Michu Bogacki", "Czarek Wieczorek", "Marta Kacprzak", "Staszek Piotrkowski", "Pawel Nowaczyk"]

print("Ania Kowalska" in moi_znajomi)
print("Grzegorz Strelczyk" in moi_znajomi)
moi_znajomi.append("Grzegorz Strzelczyk")
print(moi_znajomi)
del moi_znajomi[3]
print(moi_znajomi)
moi_znajomi.remove("Marta Kacprzak")
print(moi_znajomi)
"""
moi_znajomi = ["Marta Kacpryk", "Jedrzej Bryll"]
nowy_znajomy_1 = input("Moj nowy znajomy nazywa sie... ")
nowy_znajomy_2 = input("Moj nowy znajomy nazywa sie... ")
nowy_znajomy_3 = input("Moj nowy znajomy nazywa sie... ")
nowy_znajomy_4 = input("Moj nowy znajomy nazywa sie... ")
nowy_znajomy_5 = input("Moj nowy znajomy nazywa sie... ")
"""
moi_znajomi.append(nowy_znajomy_1)
moi_znajomi.append(nowy_znajomy_2)
moi_znajomi.append(nowy_znajomy_3)
moi_znajomi.append(nowy_znajomy_4)
moi_znajomi.append(nowy_znajomy_5)

moi_znajomi.append([nowy_znajomy_1, nowy_znajomy_2, nowy_znajomy_3, nowy_znajomy_4, nowy_znajomy_5])
print(moi_znajomi)
"""
moi_znajomi.extend([nowy_znajomy_1, nowy_znajomy_2, nowy_znajomy_3, nowy_znajomy_4, nowy_znajomy_5])
print(moi_znajomi)
