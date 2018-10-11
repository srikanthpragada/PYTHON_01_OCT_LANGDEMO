def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def math_op(n1, n2, op):
    return op(n1, n2)


print( math_op(10,20,add))
print( math_op(10,20,sub))