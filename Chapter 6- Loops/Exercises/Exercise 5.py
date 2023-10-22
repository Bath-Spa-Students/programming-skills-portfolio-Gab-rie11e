sandwich_orders = ['cheese' , 'quarter pounder' , 'ham' , 'pastrami']
finished_orders = []

print("I'm sorry, unfortunately we're out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    currrent_sandwich = sandwich_orders.pop()
    print("We're preparing your " + currrent_sandwich + " sandwich.")
    finished_orders.append(currrent_sandwich)

print('\n')
for sandwich in finished_orders:
    print("Your " + sandwich + " sandwich is done.")