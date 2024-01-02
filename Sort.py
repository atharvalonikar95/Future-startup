
nums =[]
k = int(input("Enter number of elements : "))

for i in range(0, k):
    ele = int(input())
    nums.append(ele)
n=len(nums)

for i in range(n):   
    for j in range(0,n-i-1):
        
        
        if nums[j]>=nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp
        


print(nums)
