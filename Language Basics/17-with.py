# The with statement is used in Python for resource management or context manager and clean-up actions.

# Think of it as a way to say:

# “I want to use this thing for a short time, and when I’m done, 
# make sure everything is cleaned up properly—no matter what happens.”


# class MyContext:
#     def __enter__(self):
#         print("Entering the context")
#         return self  # Optional, can return anything

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exiting the context")

# with MyContext() as m:
#     print("Inside the block")


# Context manager

class Open_File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self,exc_type,exc_val,taceback):
        self.file.close()

with Open_File('error.txt','r') as f:
    da = f.read()
    print(da)
