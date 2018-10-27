
with open("phones.txt","r") as f:
    phones = set()

    for line in f.readlines():
        input_phones = line.strip("\n").split(",")
        for phone in input_phones:
            if phone.isdigit():
                phones.add(phone)


for phone in sorted(phones):
    print(phone)



