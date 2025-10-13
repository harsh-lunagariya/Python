# pos = -1
def linearSearch(list,n):
    for i in range(len(list)):
        if list[i]==n:
            # globals()['pos'] = i+1
            return True
        
    return False 

list = [1,4,6,8,3,7,10,23,76]
n=76

print("Element found") if linearSearch(list,n) else print("not found")


# Example
# Find the first non repeating element from the list with linear search

list = [4, 5, 1, 2, 0, 4, 5, 2]
# solution
def sol(lst):
    for i in range(len(lst)):
        ct=0
        for j in range(len(lst)):
            if lst[i]==lst[j] and i!=j:
                ct += 1
        if ct == 0:
            return lst[i]
    return None

print(sol(list))
