filmy = ["Titanic", "Dirty Dancing", "Krol Lew", "Spiaca Krolewna", "Iniemamocni", "Spiderman", "Britanic", "Swieta Wojna"]
element = ["Renifer Niko ratuje Swieta"]

if element in filmy:
    print filmy
else:
    filmy.extend(element)
    del filmy[4]
    print (filmy[4])
    nowy_element = input("Podaj tytul filmu...")
    if nowy_element in filmy:
        print("Film jest juz na liscie")
    else:
        filmy.extend([nowy_element])
        print filmy
