class MyTime:
    def __init__(self, *, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property
    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)

    def __eq__(self, other):
        print("__eq__")
        return self.h == other.h and self.m == other.m and self.s == other.s

    @property
    def hours(self):
        return self.h

    @hours.setter
    def hours(self, value):
        if value >= 0 and value <= 23:
            self.h = value


t1 = MyTime(h=10, m=10, s=10)
t1.hours = 30
print(t1.hours)

print(t1.totalseconds)

t2 = MyTime(h=10, m=10, s=10)
t3 = MyTime(h=10, m=10, s=10)

print(t1 == t2)
print(t1 != t3)

print(t1)  # t1.__str__()