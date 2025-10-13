# List
lst = [1,2,3,4]
abc = ["apple","banana","cherry"]
lists = [[]]*3
# When you multiply a list by a number (e.g., * 3), it doesn't 
# create independent copies of the lists; instead, it repeats the same object 
# reference multiple times.
lists2 = [[] for _ in range(3)]
# This uses a list comprehension to create 3 independent empty lists.
# Now each sublist is a separate object in memory.

lst.append(5)
lst.extend([5,6])
lst.insert(1, "one")
lst.remove("one")
x = lst.pop(3) #return value
print(lst.count(1)) #count of 1 from list
print(lst*3) # equivalent to adding s to itself 3 times 
# [1, 2, 3, 5, 5, 6, 1, 2, 3, 5, 5, 6, 1, 2, 3, 5, 5, 6]

lst.reverse()
lst.sort()
lst1 = lst.copy()   # list is copy in different memory location
print(id(lst),id(lst1))
lst.clear()
print(", ".join(abc))
print(min(lst1) , max(lst1), sum(lst1))
lists[0].append(1)      #[[1], [1], [1]]
lists2[0].append(1)     #[[1], [], []]
print(lists)
print(lists2)

#tuple : Are immutable 
a = (10,20,30,40,50)
b = tuple()
c = (1,)
print(type(b),type(c))
# same list functions : len, min, max, sum, sorted, index, count 