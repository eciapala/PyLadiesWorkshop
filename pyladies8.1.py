vowel = ('e', 'a', 'i', 'o', 'u', 'y')
week_days = ('poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela')
months = ('styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien')
three_musketeers = ('Atos', 'Portos', 'Aramis')

print(week_days[3])
print(len(week_days))
for day in week_days:
    print(day)

tuple_vowel=tuple(vowel)

imie = input('Podaj imie: ')

if imie.capitalize() in three_musketeers:
    print('Witaj muszkieterze!')
else:
    print('Chyba nie jestes muszkieterem')

day = input('Podaj jaki jest dzisiaj dzien tygodnia: ').lower()
if day in week_days:
    if day == 'sobota' or day == 'niedziela':
        print('Yeah! Juz weekend!')
    else:
        x = 4 - week_days.index(day)
        print('Do weekendu zostalo {} dni'.format(x))