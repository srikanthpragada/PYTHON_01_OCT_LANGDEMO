# Sort names given by user

names = []  # Empty list
while True:
    name = input("Enter a name [end to stop] :")
    if name == "end":
        break

    names.append(name)

# Print names in sorted order

for n in sorted(names):
    print(n)

