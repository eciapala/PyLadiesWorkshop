friends = {
   'michu86': {
       'name': 'Michał',
       'city': 'Poznań'
   },
   'olenka': {
       'name': 'Ola',
       'city': 'Kraków'
   },
   'frodo92': {
       'name': 'Bartek',
       'city': 'Berlin'
   },
   'buziaczek': {
       'name': 'Tomek',
       'city': 'Poznań'
   },
   'lubie_pierogi': {
       'name': 'Ola',
       'city': 'Gdańsk'
   },
}
#print(friends['lubie_pierogi']['name'])

for friend in friends:
    print(friends[friend]['name'] + ' mieszka w ' + friends[friend]['city'])
