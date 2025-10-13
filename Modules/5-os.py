# It provides a way to interact with the operating system
# File and directory operations
# Environment variable access
# Process management
# Working with paths

import os
from datetime import datetime

x = dir(os)
print(len(x))

print(os.getcwd())  # it give current working dir
os.chdir('/home/harsh/Python/Program/Modules')     # it change working dir

# os.mkdir("New folder")    # use for single dir
# os.makedirs("one/two")    # use for multiple dir

# os.rmdir("New folder")
# os.removedirs("one/two")

print(os.listdir('/home/harsh/Python/Program/DSA')) # default '.'

val = os.walk(os.getcwd())

for cur_dir,list_dir,list_files in val:
    print(f'{cur_dir}\t{list_dir}\t{list_files}')

status = os.stat('/home/harsh/Python/Program/Assignment/Harsh_Assignment1.py')

print("Last Modified :",datetime.fromtimestamp(os.path.getmtime('/home/harsh/Python/Program/Assignment/Harsh_Assignment1.py')))

print(os.path.basename('temp/abc.txt'))     # return basefile name for this abc.txt
print(os.path.dirname('temp/one/ar.txt'))   # return dir name
print(os.path.split('temp/one/ar.txt'))   # split dir and file
print(os.path.exists('temp/one/ar.txt'))   
# os.path.isfile()
# os.path.isdir()
print(os.path.join('home','harsh','Python'))       # home/harsh/Python
pth = '5-os.py'
print(os.path.abspath(pth))     # home/harsh/Python/Program/Modules/5-os.py
print(os.system('clear'))
# print(os.environ)
print(os.getenv('SESSION_MANAGER'))
print(os.name)
os.mkdir('oneworld')
os.rename('oneworld','twoworld')