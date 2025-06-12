class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Usman", 50000, "123-45-6789")

print(emp.name)              # Public
print(emp._salary)           # Protected
print(emp._Employee__ssn)    # Private (using name mangling)