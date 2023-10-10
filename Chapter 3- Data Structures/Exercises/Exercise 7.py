countries = ["Japan" , "South Korea" , "Switzerland" , "Norway" , "New Zealand"]

print("\nOriginal")
print(countries)

print("\nAlphabetical")
print(sorted(countries))

print("\nOriginal")
print(countries)

print("\nReverse Alphabetical")
print(sorted(countries, reverse=True))

print("\nReversed")
countries.reverse()
print(countries)

print("\nOriginal")
countries.reverse()
print(countries)

print("\nAlphabetical")
countries.sort()
print(countries)

print("\nReverse Alphabetical")
countries.sort(reverse = True)
print(countries)