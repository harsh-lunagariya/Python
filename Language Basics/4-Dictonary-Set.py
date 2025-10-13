# Dictionary : Key value pair
dic = {'name':'Harsh','age':21,'country':"India"}

print(dic.get('name'))
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.update({'age':22})) 
dic.pop('country')
dic1 = dic.copy()
dic1.clear()
print('name' in dic)

# Set : Unordered, Unchangeable, no duplicates
a = {1,3,5,6,7,8,8,8}
b = set()
print(type(b))

# Methods : add, remove, clear, copy, union, intersection, difference, issubset, issuperset, isdisjoint


# Frozen set - are immutable object, it have characteristics of a set, but its elements can not change after assign
lst = [1,2,3,4,5,5,6]
froz = frozenset(lst)
print(froz)
# Use - Since sets are mutable and un-hashable, they can't be used as key in dictonary
# but frozen set are hashable and can be use as a key in dictonary