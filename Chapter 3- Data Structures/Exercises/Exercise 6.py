names =["Amy" , "Holt" , "Jake"]
print(names[0] + " I would like to invite you at an Italian restaurant tonight for a delighful dinner.")
print(names[1] + " I would like to invite you at an Italian restaurant tonight for a delighful dinner.")
print(names[2] + " I would like to invite you at an Italian restaurant tonight for a delighful dinner.")
print("\nUnfortunately It seems like", names[1], "will not be able make it.")

del(names[1])
names.insert(1 , "Charles")

print(names[0] + " I would like to invite you at an Italian restaurant tonight for a delighful dinner.")
print(names[1] + " I would like to invite you at an Italian restaurant tonight for a delighful dinner.")
print(names[2] + " I would like to invite you at an Italian restaurant tonight for a delighful dinner.")

print("\nUnfortunately the table that the restaurant limits the people I can invite. I'm sorry", names[1] + ".")

names.pop(1)
print(names)

print(names[0], ", I would like to invite you to dinner")
print(names[1], ", I would like to invite you to dinner")

names.pop(0)
print(names)

names.pop(0)
print(names)