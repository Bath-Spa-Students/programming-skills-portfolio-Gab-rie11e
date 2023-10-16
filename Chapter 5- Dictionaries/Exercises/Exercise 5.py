pets = []

pet = {
    'animal type': 'cat',
    'name': 'tiger',
    'owner': 'john',
    'weight': '10 pounds',
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'bruno',
    'owner': 'isabella',
    'weight': '30 pounds',
    'eats': 'dog food',
}
pets.append(pet)

pet = {
    'animal type': 'bunny',
    'name': 'snowball',
    'owner': 'kevin',
    'weight':'4 pounds',
    'eats': 'lettuce',
}
pets.append(pet)

for pet in pets:
    print("\nWhat I know about " + pet['name'].title() + ":")
    for key, value  in pet.items():
        print("\t" + key + ": " + str(value))