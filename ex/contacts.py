import re

f = open("contacts.txt", "rt")
persons = []
for line in f.readlines():
    parts = line.strip("\n").split(",")
    if len(parts) < 3:
        continue

    name = age = mobile = None
    for p in parts:
        p = p.strip(" ")
        m = re.fullmatch("[A-Za-z ]+", p)
        if m:
            name = m.group()
            continue

        m = re.fullmatch(r"\d{10}", p)
        if m:
            mobile = m.group()
            continue

        m = re.fullmatch(r"^\d{2,3}$", p)
        if m:
            age = m.group()

    if name and mobile and age:
        persons.append((name, mobile, age))


for p in sorted(persons, key=lambda v: v[2]):
    print(p)
