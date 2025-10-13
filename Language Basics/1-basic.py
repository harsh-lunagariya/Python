# Single line comment

"""Multi
line 
comment"""

a = 30 # variables = container to store a value. <int>
b = "Harsh" # <str>
c = 71.22 # <float>
d = True # <bool>
e = None # <NoneType>
f = 2 + 3j #<complex>
... # <ellipsis> it is expression , placeholder 
pass # do nothing , it is statement

# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.

x,y = divmod(10,3)      # It give tuple of quotient and remainder (3,1)
# 1//2 is 0, (-1)//2 is -1, 1//(-2) is -1, and (-1)//(-2) is 0

print(type(d),type(e),type(f),type(...))

#Type Casting
str(32)
int("32")
float(32)

#Input
A = input("Enter a number : ")  #It always input in str

# Bitwise Operation
print(~12) #complement
print(12 & 13) #and
print(12 | 13) #or
print(12 ^ 1) #xor
print(10 << 2) #left shift
print(10 >> 1) #right shift