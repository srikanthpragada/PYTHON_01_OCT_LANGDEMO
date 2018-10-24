# Superclass
class Employee:
    da = 5000

    def __init__(self, empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary + Employee.da

    def get_name(self):
        return self.name


# Subclass
class Manager(Employee):
    def __init__(self, empno, name, salary, hra):
        # Employee.__init__(self, empno, name, salary)
        super().__init__(empno, name, salary)
        self.hra = hra

    # Overriding
    def get_salary(self):
        return super().get_salary() + self.hra


e = Employee(1, "Jack", 100000)
m = Manager(2, "Steve", 150000, 50000)

print(e.get_salary())
print(m.get_salary())
print(m.get_name())
