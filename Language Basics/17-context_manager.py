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


# Context manager - theoritycal

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

# context manager

from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
    try:
        f = open(file,mode)
        yield f     # run all above code, when the execution complete of with block then the fun executes code after yield
    finally:
        f.close()

with open_file('error.txt','r') as f:
    da = f.read()
    print(da)

# Example use of context manager

import os

# cwd = os.getcwd()
# os.chdir('Modules')
# print(os.listdir())
# os.chdir(cwd)

# The below code does same thing with context manager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('Modules'):
    print(os.listdir())

