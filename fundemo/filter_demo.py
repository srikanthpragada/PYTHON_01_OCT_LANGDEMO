def is_even(n):
    return n % 2 == 0


l = [10, 20, 30, 33, 44, 11]

en = filter(is_even, l)
for n in en:
    print(n)

odn = filter(lambda n: n % 2 == 1, l)
for n in odn:
    print(n)
