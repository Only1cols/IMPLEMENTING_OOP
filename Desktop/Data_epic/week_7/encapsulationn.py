# encapsulation means hiding int.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ernal details of a class and only expoing whats necessary
# encapsulation i done by adding a double underscore after self.... eg self.__salary
# this way, salary is hidden and not accessible eg


class Employee:
    def __init__(self, name, salary):
        self.name = name  # public attribute
        self.__salary = salary  # private attribute


emp = Employee("Ebuka", 50000)
print(emp.name)
# print(emp.__salary)

# so when you run this program, emp.__salary would give an error, because it is encapsulated  i.e it is made private


# Public members
,