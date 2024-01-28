nums=[]
def add(num):
    
    num=str(num)
    

    for i in num:
        nums.append(int(i))
    # print(nums)
    # print(len(nums))

    sum=0
    for i in range(len(nums)):
        sum=sum+nums[i]
    nums.clear()
    # print(nums)
    return sum
print(add(32))
if len(str(add(32)))>1:
    print(add(add(32)))
