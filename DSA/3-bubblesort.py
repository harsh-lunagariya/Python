def sort(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

nums = [5,3,8,33,6,1,2,54]
sort(nums)
print(nums)


# Example
# simulate bubble sort and return the number of swaps required to bring the
# smallest k elements to their correct positions in the array

def sol(arr,k):
    n=len(arr)
    count=0
    for i in range(k):
        for j in range(n-1,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                count+=1
    return count


arr = [7, 3, 2, 4, 5, 1]   
k = 3

print(sol(arr,k))
print(arr)

