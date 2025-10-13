
# Count and return the total number of swaps that would be performed
# only during the first m iterations of the outer loop
def sort(nums,m):
    n=len(nums)
    ct=0
    for i in range(min(m,n-1)):
        min_idx=i
        for j in range(i+1,n):
            if nums[j]<nums[min_idx]:
                min_idx = j
        if i!=min_idx:
            nums[i],nums[min_idx] = nums[min_idx],nums[i]
            ct+=1
        
    return ct


arr = [29, 10, 14, 37, 13]
m = 3

x=sort(arr,m)
print(arr,x)