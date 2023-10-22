prompt = "How old are you?"

while True:
    age = input(prompt)
    if age == 'quit':
       break
    age = (int(age))

    if age < 3:
        print("You're ticket is free!")
    elif age < 12:
        print("Your ticket will cost $10")
    else:
        print("Your ticket will cost $15")