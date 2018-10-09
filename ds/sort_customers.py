# Sort names given by user

custs = {}  # Empty dict
while True:
    name = input("Enter a name [end to stop] :")
    if name == "end":
        break

    mobile = input("Enter a mobile number :")
    custs[name] = mobile

# Print customers in sorted order
for n, m in sorted(custs.items()):
    print('%-20s %s' % (n, m))
