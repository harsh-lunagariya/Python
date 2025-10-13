class Student:
    name = 'ACB'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def getSchool(cls,a=2):
        return cls.name,a

    @staticmethod
    def info():
        print("This is student .!.")

s1 = Student(65,86,87)
print(s1.avg())
print(Student.getSchool())
Student.info()

# Inner Class
class Student:
    def __init__(self,name,RollNo):
        self.name = name
        self.RollNo = RollNo
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.RollNo)
        self.lap.show()
    
    class Laptop:
        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Harsh',18)
s1.show()
s2 = Student('ZAD',20)
s2.show()

# Abstract Class
from abc import ABC,abstractclassmethod

class Computer(ABC):
    @abstractclassmethod
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print("Processing...")

a=Laptop()
a.process()


# Inheritance
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1")

class B(A):
    def __init__(self):
        super().__init__()  
        print("in B init")
    def feature3(self):
        print("Feature 3 from B")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("From C class")
    
    def feature5(self):
        print("Feature 5")

b=C()


# Operator Overloading
class A:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=A(m1,m2)
        return s3
    
    def show(self):
        print(self.m1, self.m2)

s1 = A(80,90)
s2 = A(61,42)
a=1
s3 = s1+s2 
b=a.__str__()
s3.show()