def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i

    return f


def factorials():
    for n in range(1, 10):
        yield factorial(n)


facts = (factorial(n) for n in range(1, 10))

for n in factorials():
    print(n)
