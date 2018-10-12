def fun(n):
    print(id(n))
    n = 0
    print(id(n))


def fun2(lst, v):
    lst.append(v)


a = 10
print(id(a))
fun(a)
print(id(a))
print(a)

l = [10,20]
fun2(l,30)
print(l)

