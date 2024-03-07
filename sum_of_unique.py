nums=[1,2,3,1]
ans=[]
for i in range (len(nums)):
    count=1
    for j in range(len(nums)):
        if nums[i]==nums[j] and i!=j:
            count+=1
for i in nums:
    if i.==1:
       ans.append(i)
    print(ans)