rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'yenisei': 'russia',
}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")