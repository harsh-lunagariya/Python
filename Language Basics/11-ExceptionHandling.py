a=5
b=0

try:
    print("Resource open..")
    print(a/b)
    k = int(input("Enter a number : ")) # This will not run if b is 0
    print(k)

except ZeroDivisionError:
    print("Can not divide by zero")

except ValueError:
    print("Invalid value")

except Exception as e:
    print("Something went wrong",e)

finally:
    print("Resource close\n\n")

# Handle in import block
try:
    import some  # type: ignore for this time
except ImportError:
    print("some module not found\n\n")

# Custom exception and raise exception

class Custom(Exception):
    "This is my custom exception block"
    pass

try:
    raise Custom
except Custom:
    print("Handle custom exception")


