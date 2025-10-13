import sys

# Command line argument - argv
print(type(sys.argv))   # list
print("size of atgv",len(sys.argv))
print("Values in argv",sys.argv,end='\n\n')

# Python path
print(sys.path,end='\n\n')

# imported modules
print(len(sys.modules))  # It gives imported modules in dictonary format

# largest supported length of container
print(sys.maxsize)
# mylist = list(range(sys.maxsize+2))

# python version and information
print(sys.version)
print(sys.version_info)

# system platform information
print(sys.platform)

# stdin
# for words in sys.stdin:
#     if 'quit'==words.strip():
#         break
#     print(f'Input : {words}')
# print("Exit")

# stdout stderr
sys.stdout.write("Harsh\n")
sys.stderr.write("Harsh patel")

# sys.stdout = open("output.txt",'w')
# sys.stderr = open("error.txt",'w')

# # Normal statement is print in output.txt
# print("This is standerd output")

# try:
#     1/0
# except ZeroDivisionError as e:
#     print(f"Error occured : {e}",file=sys.stderr)

# sys.stdout.close()
# sys.stderr.close()



# Functions

# exit the program
# sys.exit(0)
# for i in range(100000000):
#     print(i)
#     if i==8:
#         sys.exit("somthing")


# Size of an object in byte
a=10
print(sys.getsizeof(a))

# Recursion Limit
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

# Switch interval time - amount of time the Python interpreter waits before switching
# between threads when using Python's threading module.
print(sys.getswitchinterval())

