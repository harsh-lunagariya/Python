# Question 1 and 3


import json
try:
    with open("students.json","r") as f:
        students = json.load(f)
    
except FileNotFoundError:
    students = {}


while True:
    res = input("For entering detail press y : ") 
    if res.lower() != 'y':
        break

    student_id = input("Enter Student ID : ")
    name = input("Enter student name : ")

    while True:
        try:
            age = int(input("Enter student age : "))
            if age > 100 or age < 0 : 
                raise ValueError()
            break
        except (ValueError, Exception):
            print("Enter valid age")  
            
    while True:
        try:
            marks = int(input("Enter student marks : "))
            if marks<0 or marks>100:
                raise ValueError()
            break
        except (ValueError, Exception):
            print("Enter valid marks")

    students[student_id] = {'name':name, 'age':age, 'marks':marks}
    print()

with open("students.json","w") as f:
    json.dump(students,f,indent=4)

def show():
    print("\n")
    for id in students.keys():
        print(f"Student ID : {id} \tName : {students[id]['name']} \tAge : {students[id]['age']} \tMarks : {students[id]['marks']}")
    print("\n")

def maxMarks():
    if len(students)==0:
        print("Student table is empty")
        return
    
    max = -1
    sid = None

    for id in students.keys():
        if max<students[id]['marks']:
            sid = id
            max=students[id]['marks']
    
    print(f"Name : {students[sid]['name']}  Marks : {max}")

def avgMarks():
    if len(students)==0:
        print("Student table is empty")
        return
    sum = 0
    ct=0
    for id in students.keys():
        sum += students[id]['marks']
        ct+=1
    avg = sum/ct
    print(f"Average marks of all student is {avg:.2f}")


show()
maxMarks()
avgMarks()



# Question 2

str = 'Alexandere'
str = str.lower()

dic = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}

vowel = 0
for i in range(len(str)):
    if str[i] in dic.keys():
        dic[str[i]] = dic[str[i]]+1
        vowel+=1

print(f"Vowels = {vowel}    Consonants = {len(str)-vowel}")

for key, value in dic.items():
    if value != 0:
        print(f"{key} : {value}")

x = max(dic.values())

print("Highest repeating vowel")

for key,value in dic.items():
    if x == value:
        print(f"{key} : {value} ")