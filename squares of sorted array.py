class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in range(len(nums)):
            sq=nums[i]*nums[i]
            l1.append(sq)
        l1.sort()
        return l1
        