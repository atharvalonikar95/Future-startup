class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        iterations = 0

        while any(nums[i] > 0 for i in range(len(nums))):
            nums.sort()

            min1 = None
            for i in range(len(nums)):
                if nums[i] > 0:
                    min1 = nums[i]
                    break

            if min1 is not None:
                for i in range(len(nums)):
                    if nums[i] > 0:
                        nums[i] = nums[i] - min1

            iterations += 1
        return iterations
        