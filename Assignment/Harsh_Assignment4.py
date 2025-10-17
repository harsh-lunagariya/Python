s = input("Input :")

# first approach - long array adding
temp = str()
lst = list()

for i in range(len(s)):
    if s[i]==' ' and s[i-1]!=' ':
        lst.append(temp)
        temp=''
        pass
    temp += s[i]

lst.append(temp)

for i in lst[::-1] : 
    i = i.strip()
    print(i,end=' ')
print()

# Second approach - insert method

lst = s.split()
output = []
for i in lst:
    output.insert(0,i)
output = ' '.join(output)
print(output)

# third - list swapping

start=0
end=len(lst)-1

while end>start:
    lst[start],lst[end] = lst[end],lst[start]
    start+=1
    end-=1

for i in lst:
    print(i,end=' ')
print()

# 4th - stack
from collections import deque

lst = s.split()
stack = deque()

for i in lst:
    stack.append(i)

temp=''
for i in range(len(lst)):
    temp += stack.pop() + " "

print(temp)

# 5th - reverse list method
lst = s.split(" ")
for i in reversed(lst):
    print(i,end=' ')