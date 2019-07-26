class Person:
    # GLOBAL_COUNT = 0
    def __init__(self, n = "B", a= "30"):
        self.full_name = n
        self.age = a        
        self.x = 5
        self.__class__.GLOBAL_COUNT = 2
    def GLOBAL_INCREMENTER(self):
        self.__class__.GLOBAL_COUNT += 1
    def get_age(self):
        return self.age
    def print_out(self):
        print(self.full_name, "is", self.age, "years old", "and global_count", self.GLOBAL_COUNT)
    def set_age(self, age):
        self.age = age
    def set_name(self, name):
        self.full_name = name

class Student:
    def __init__(self, n, a):
        self.full_name = n
        self.age = a
    
    def get_age(self):
        return self.age

class Employee:
    def __init__(self, n, a, d, s):
        self.name = n
        self.age = a
        self.designation = d
        self.salary = s

    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name

    def get_designation(self):
        return self.designation
    
    def get_salary(self):
        return self.salary
    
    def set_age(self, age):
        self.age = age
    
    def set_name(self, name):
        self.name = name

    def set_designation(self, designation):
        self.designation = designation

    def set_salary(self, salary):
        self.salary = salary

    def print_out(self):
        print(name, "is", self.age, "years old", "and is a", self.designation, "making $", self.salary)

if __name__ == "__main__":
    obj = Person()
    obj.print_out()
    obj.set_age(25)
    obj.set_name("Greg Anthony")
    obj.print_out()
    print(obj.full_name)
    print(obj.age)
    obj2 = Person()
    obj.GLOBAL_INCREMENTER()
    obj.GLOBAL_INCREMENTER()
    obj.GLOBAL_INCREMENTER()
    obj.GLOBAL_INCREMENTER()
    print(obj.GLOBAL_COUNT)
    obj.print_out()
    
    print(obj2.GLOBAL_COUNT)