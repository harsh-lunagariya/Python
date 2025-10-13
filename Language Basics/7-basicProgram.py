# Prime number
n = 7

for i in range(2,n):
    if n%i == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is prime number")

#Factorial
n=6
fact = 1
if i<=1:
    pass
else:
    for i in range(2,n+1):
        fact *= i

print("Factorial :",fact)

# Arm strong number
# n = int(input("Number between 100 and 1000 : "))

a=100
lst = list()
while a<=1000:
    n=a
    arm = 0
    while n!=0:
        x = n%10
        arm = arm+x**3
        n = n//10
    if a==arm:
        lst.append(a)
        print(a)
    a += 1
print(lst)