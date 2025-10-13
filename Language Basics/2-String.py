# Strings are immutable object it can not change

a = 'Python functions' #single quoted
b = "Harsh" #double quoted
c = """This 
is 
a program""" #use for multiline string
d="     Hello, World!      "
e="apple banana mango"

print(b[3])
print(a[1:10:2])
print(b[::-1]) #Reverse string

print(len(a))
print(b.upper())
print(b.lower())
print(a.title())
print(e.capitalize())
print(d.strip())    #removes before and after space ,trim
print(d.replace("World","Harsh"))
print(e.split())
print(b.startswith("Ha")) # same for endswith()
print("hello1867".isalpha()) # same for isdigit()
print("my name is {} and I am {} year old".format(b,21))
print(a.removeprefix("Py"))
print(a.removesuffix('functions'))
print('python'.center(10))
print('python'.center(12,'-'))