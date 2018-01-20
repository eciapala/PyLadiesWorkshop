friends_home = {
    'Michal': 'Poznan',
    'Ola': 'Krakow',
    'Bartek': 'Berlin',
    'Tomek': 'Poznan'
}

print(friends_home)
ola_home = friends_home['Ola']
print(friends_home)
friends_home['Ola']:'Kijow'
print(friends_home)
friends_home['Grzes']:'Poznan'
print(friends_home)
del friends_home['Tomek']
print(friends_home)
friends_home.clear()
print(friends_home)

