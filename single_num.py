nums=[]
k=int(input("enter number of elements:"))
for i in range(0,k):
    E=int(input())
    nums.append(E)
n=len(nums)
for i in range (0,n):
    count=0
    for j in range(0,n):
        if nums[i]==nums[j] and i!=j:
            count+=1
    if count==0:
        print("Single Element found in nums is :",nums[i])
        break
            
