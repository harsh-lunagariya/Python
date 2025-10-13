# If else
condition = True
if(condition == True):
    print("pass")
elif(condition != True):
    print("elif pass")
else:
    print("else pass")

# Single line if else
# value_if_true if condition else value_if_false
x = 12
print("Is adult") if x>=18 else print("Is child")

# Loop
i = 0
while i<10:
    i = i+1
    if i == 3:
        continue
    elif i == 5:
        break
    else:
        pass
    print("Execute")
    
for i in range(2, 11 ,2):
    print(i)
else:
    print("complete")

# Throw away variable
# when you no need to care about i or iterable in for loop then use _ 

for _ in range(5):
    print("Hello")

# enumerate function : use for indexing in loop

mark = [60, 30, 60, 70, 80, 30, 60, 80, 50]

for index, mark in enumerate(mark):
    print(index,mark)


# Match case like Switch case

age = 20

match age:
    case a if a < 18:
        print("Minor")
    case a if 18 <= a < 60:
        print("Adult")
    case _:     #default case
        print("Senior")
