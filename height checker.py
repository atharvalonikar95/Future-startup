class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=[]
        for i in heights:
            expected.append(i)
        expected.sort()

        count=0
        for i in range(len(expected)):
            if heights[i]!=expected[i]:
                count+=1
        return count
