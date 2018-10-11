
def print_names(*names, message= "Hello"):
    print(type(names))
    for n in names:
        print(message, n)


print_names("Abc","Xyz","Pqr")
print_names("Abc","Def",message = "Good Evening")
