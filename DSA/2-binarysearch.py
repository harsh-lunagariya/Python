list = [1,4,6,8,10,23,76]

def search(lst, n):
    l=0
    u=len(lst)-1

    while l<=u:
        mid= (l+u) // 2
        if lst[mid]==n :
            return True, mid
        else:
            if lst[mid]>n :
                u=mid-1
            else:
                l=mid+1
    return False,-1

x,y = search(list,76)

if x:
    print("Element found at ",(y+1))
else:
    print("not found")

# With recursion
def searchRec(lst,n,l,u):
    if l>u:
        return -1
    mid = (l+u)//2
    if lst[mid]==n:
        return mid
    elif lst[mid]>n:
        return searchRec(lst,n,l,mid-1)
    else:
        return searchRec(lst,n,mid+1,u)

print("Element found at",searchRec(list,100,0,len(list)-1))

# Example
# Find the first occurrence of element from the list with using binary search

arr = [1, 2, 4, 4, 4, 5, 5, 6]

def searchSol(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n and list[mid-1]!=n:
            return mid
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return -1

print(searchSol(arr,6))