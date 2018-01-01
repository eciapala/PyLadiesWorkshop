"""
pusta_lista = []
lista_liczb = [34, 45.5, 67, 0, -30, 40+5]
lista_stringow = ["jablko", "banan", "gruszka"]
lista_list = [[34, 45], [56, 78.9]]
lista_zmiennych = [lista_liczb, lista_stringow, lista_liczb]
lista_mix = ["python", [56, 78, "mysz"], lista_liczb, "pizza"]
#print (lista_mix)
"""
lista_stron = [23, 5, 43, 0, 0, 5, 0, 32, 67]
liczba_dni = len(lista_stron)
#print (liczba_dni)

#dzien_ostatni = lista_stron[8]
#print (dzien_ostatni)

dzien_ostatni = lista_stron[len(lista_stron) - 1]
print (dzien_ostatni)

lista_stron[3:]
lista_stron[2:4]
lista_stron[:3]

pierwsze_3_dni = lista_stron[:3]
print(pierwsze_3_dni)
