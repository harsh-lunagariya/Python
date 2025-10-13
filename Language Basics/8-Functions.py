def fact(n:int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))



# Return type and argument type
def greet(name: str) -> str:
    return f"Hello, {name}"
# -> return type
# : argument type



#lambda
sq = lambda x : x*x
print(sq(5))



# Variable length argument
def sum(*a):
    c = 0
    for i in a:
        c += i
    return c

print(sum(1, 2, 3, 4, 5, 6, 7, 8))



# Keyword variable length argument
def person(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)

person('harsh',age = 20,city = 'rajkot',mob=9977659278)



# Global variable
a = 10

def something():
    a = 9
    print("In fun ",a)
    globals()['a'] = 15

something()
print("In main ",a)



# Filter
from functools import reduce
nums = [1,2,3,4,5,7,8,9,6]

evens = list(filter(lambda a : a%2==0 ,nums))
doubles = list(map(lambda a : a*a,evens))
print(doubles)
sum = reduce(lambda a,b : a+b , doubles)


print(sum)



# Recursive lambda

fact = lambda x : 1 if x == 1 else x * fact(x-1)



# Decorators 
def decorators(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorators
def simple():
    print("Hello world!")

simple()

if __name__ == "__main__":
    print("In main module")

