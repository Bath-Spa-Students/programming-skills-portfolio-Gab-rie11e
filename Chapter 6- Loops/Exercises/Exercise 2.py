prompt = "How old are you?"

# I proceed to write a code where the system asks for the user input 
while True:
    age = input(prompt)
    age = (int(age))

# Input gets processed and compared from all the lines to find the right one to print
    if age < 3:
        print("You're ticket is free!")
    elif age < 12:
        print("Your ticket will cost $10")
    else:
        print("Your ticket will cost $15")