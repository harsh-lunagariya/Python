f = open("simple.txt",'r')

f1 = open("simple.txt","a")

with open("simple.txt",'w') as f3:
    f3.write("Only me")

# r+  :   read + write
# a+  :   append + read
# w+  :   write + read


# read and write binary file

f.close()
f1.close()

f = open("img.jpg",'rb')

f1 = open("myImg.jpg",'wb')

for i in f:
    f1.write(i)

f.close()
f1.close()

# Handle exception

try:
    with open("img.jpg",'rb') as f:
        for i in f:
            print(i,end='')
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You not have permission to read the file")
except Exception as e:
    print("Error accrued {}".format(e))
