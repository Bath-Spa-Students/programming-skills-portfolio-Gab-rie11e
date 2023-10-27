# Created a loop about making pizza
prompt = "What toppings would you like? "
prompt  += "\nType 'quit' when you're done choosing: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("I'll put " + topping + " in your pizza")
    else:
        break 
