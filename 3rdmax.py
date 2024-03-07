#            method 1

# class Solution:
#     def thirdMax(self, NUMS: List[int]) -> int:
   
#         nums=set(nums)
#         nums=list(nums)
        
        # nums.sort()

        # if len(nums)==2:
        #     return nums[-1]
        # elif len(nums)==1:
        #     return nums[-1]
        # elif len(nums)==0:
        #     return []
        # else :
        #     return nums[-3]

#            method 2
NUMS = [-2147483648, -2147483648, -2147483648, -2147483648, 1, 1, 1]
NUMS.sort()
i = 0
while i < len(NUMS):
    num = NUMS[i]
    if NUMS.count(num) > 1:
        NUMS.remove(num)
    else:
        i += 1

print(NUMS)


# NUMS=[1,2,3,4]# first sort the list for this solution

max1 = float('-inf')
max2 = float('-inf')
max3 = float('-inf')

def thirdmax(NUMS,max1,max2,max3):
    for i in range(len(NUMS)):
        if NUMS[i]>=max1:
            max3=max2
            max2=max1
            max1=NUMS[i]
            

    if len(NUMS)==2:
        return max1
    elif len(NUMS)==1:
        return max1
    elif len(NUMS)==0:
        return []
    else :
        return max3

    
ans=thirdmax(NUMS,max1,max2,max3)
print(ans)



# NUMS = [-2147483648, -2147483648, -2147483648, -2147483648, 1, 1, 1]

# i = 0
# while i < len(NUMS):
#     num = NUMS[i]
#     if NUMS.count(num) > 1:
#         NUMS.remove(num)
#     else:
#         i += 1

# print(NUMS)
