#here i introduce a list of kinds of sandwiches
sandwich_orders = ['cheese' , 'quarter pounder' , 'ham']
finished_orders = []

#this is where i print the orders that are currently being maded.
while sandwich_orders:
    currrent_sandwich = sandwich_orders.pop()
    print("We're preparing your " + currrent_sandwich + " sandwich.")
    finished_orders.append(currrent_sandwich)


#now here i print the finished orders.
print('\n')
for sandwich in finished_orders:
    print("Your " + sandwich + " sandwich is done.")