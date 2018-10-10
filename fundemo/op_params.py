def fun(n1, n2):
    pass


def fun2(p1=10, p2=20):
    print(p1, p2)


# Only named parameters
def fun3(*, p1=10, p2, p3=1):
    print(p1, p2, p3)


fun(10, 20)  # Positional
fun(n2=10, n1=20)  # Named
# fun(n2=100)

fun2(10, 20)
fun2(10)
fun2(p2=10)

fun3(p2=10, p1=20)
fun3(p2=100)
