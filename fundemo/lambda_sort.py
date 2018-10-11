names = ["Java", "Php", "C++", "C#", "Python", "Ruby", "c"]

for n in sorted(names, key=lambda n: len(n)):
    print(n)
