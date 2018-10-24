from abc import ABC, abstractmethod


class Doctor(ABC):  # Abstract class
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    @abstractmethod
    def get_salary(self):
        pass


class RDoctor(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def get_salary(self):
        return self.salary


d = RDoctor("Dr. James", "Ped", 100000)
print(d.get_salary())
