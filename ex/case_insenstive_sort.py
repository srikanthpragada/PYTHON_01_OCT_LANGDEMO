
names = ["java","JavaScript","c","C#","Python"]

for n in sorted(names,key=lambda n: n.upper()):
    print(n)

for n in sorted(names,key=str.upper):
    print(n)