class A:
    def m(self):
        print("In A")


class B:
    def m(self):
        print("In B")


class C(A):
    pass


class D(B,C):
    pass


obj = D()
print(D.mro())
