nums = [1, 2, 3, 4, 5, 6, 7]

k=3
# sol1
for i in range(k):
    temp=nums[-1]
    for i in range(len(nums)-1,0,-1):
        nums[i]=nums[i-1]
    nums[0]=temp

# sol2
for i in range(k):
    last=nums.pop()
    nums.insert(0,last)
print(nums)



