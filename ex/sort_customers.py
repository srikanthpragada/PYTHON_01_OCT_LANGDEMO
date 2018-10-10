# Sort customer details by name

customers = {}  # Empty dict
while True:
    name = input("Enter a name [end to stop] :")
    if name == "end":
        break

    mobile = input("Enter a mobile number :")
    if name in customers:  # customer is already found in dict
        customers[name].add(mobile)
    else:
        customers[name] = {mobile}

    # Print customers in sorted order
for name, mobiles in sorted(customers.items()):
    print('%-20s %s' % (name, ",".join(mobiles)))
