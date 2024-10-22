# Inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")
        
        
    @staticmethod
    def stop():
        print("car stopted..")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
        
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
            
        
# Multi_level Inheritance       
class Car:
    @staticmethod
    def start():
        print("car started..")
        
        
    @staticmethod
    def stop():
        print("car stopted..")
        
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

        
car1 = Fortuner("diesel")
car1.start()             
    
    
# Multiple Inheritance 
class A: 
    varA = "welcome to class A"   
    
class B: 
    varB = "welcome to class B"   
    
class C(A,B): 
    varC = "welcome to class C"    
    
c1 = C()    
    
print(c1.varC)    
print(c1.varB)    
print(c1.varA)    
    
    
# Super Method   
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started..")
        
        
    @staticmethod
    def stop():
        print("car stopted..")
        
class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()   
    
car1 = ToyotaCar("prius","electronic")
print(car1.type)   
    
    
# Class Method 
class Person:
    name = "anonymous"
    
    @classmethod
    def changeName(cls,name):
        cls.name = name
        
p1 = Person()
p1.changeName("mazhar") 
print(p1.name)
print(Person.name)    
    
# Property Decorator
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"



stu1 = Student(98, 97, 99)
print(stu1.percentage)
    
stu1.phy = 86
print(stu1.percentage)
    
    
    
    
    
    
    
    
    
    
    
    
        
        