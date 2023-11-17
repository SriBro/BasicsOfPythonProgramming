#OOP or Object Oriented Programming - helps to convert real world objects into code. Here is a sample code

class Employee:
    #we use __ so that we cannot directly access the variable outside class by an object
    __name = None
    __id = 0
    __salary = 0

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_id(self,id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_salary(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary

emp = Employee()
    
emp.set_name('Anil')
emp.set_id(1)
emp.set_salary(2000)
print(emp.get_name())
print(emp.get_id())
print(emp.get_salary())