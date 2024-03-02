#            method 1

# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
   
#         nums=set(nums)
#         nums=list(nums)
        
#         nums.sort()

#         if len(nums)==2:
#             return nums[-1]
#         elif len(nums)==1:
#             return nums[-1]
#         elif len(nums)==0:
#             return []
#         else :
#             return nums[-3]

#            method 2

NUMS=[1,2,3]

max1 = float('-inf')
max2 = float('-inf')
max3 = float('-inf')

def thirdmax(NUMS,max1,max2,max3):
    for i in range(len(NUMS)):
        if NUMS[i]>=max1:
            max3=max2
            max2=max1
            max1=NUMS[i]
        if max2>NUMS[i]>max3 :
            max2=NUMS[i]
    return max3
ans=thirdmax(NUMS,max1,max2,max3)
print(ans)


    
