class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums.sort()
        i = 0
        while i < len(nums):
            num = nums[i]
            if nums.count(num) > 1:
                nums.remove(num)
            else:
                i += 1



        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')

        for i in range(len(nums)):
                if nums[i]>=max1:
                    max3=max2
                    max2=max1
                    max1=nums[i]
        if len(nums)==2:
            return max1
        elif len(nums)==1:
            return max1
        elif len(nums)==0:
            return []
        else :
            return max3