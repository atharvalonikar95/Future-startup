class Solution:
    def thirdMax(self, nums: List[int]) -> int:
   
        nums=set(nums)
        nums=list(nums)
        
        nums.sort()

        if len(nums)==2:
            return nums[-1]
        elif len(nums)==1:
            return nums[-1]
        elif len(nums)==0:
            return []
        else :
            return nums[-3]

        

# nums=[1,1,1]

# print(type(nums))
# nums=set(nums)
# nums=list(nums)
# print(type(nums))
# nums.sort()
# print(nums)
# n= len(nums)
# if n==2:
#     print( nums[-2])
# elif n==1:
#     print( nums[-1])
# elif n==0:
#     print( [])
# else :
#     print( nums[-3])
