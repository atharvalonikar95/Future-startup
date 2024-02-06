class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output=[]
        if target not in nums:
            return [-1,-1]
        elif len(nums) == 1:  
            return [0, 0]
        for i in range (len(nums)):
            if nums[i]==target:
                output.append(i)
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                output.append(i)
                break

        return output

        