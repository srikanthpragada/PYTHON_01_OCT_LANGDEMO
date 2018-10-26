
f = open(r"e:\classroom\python\oct1\names.txt","wt")

while True:
    name = input("Enter a name [end to stop] :")
    if name == "end":
         break
    f.write(name + "\n")

f.close()
