

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        max_item, max_val = None, 0

        for i, val in dic.items():
            if val > max_val:
                max_val = val
                max_item = i

        return max_item
