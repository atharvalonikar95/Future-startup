class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()
        nums_str=[]
        for i in nums:
            nums_str.append(str(i))
        n=len(nums_str)
        
        for i in range (n):
            for j in range(n):
                if int(nums_str[j]+nums_str[i])<int(nums_str[i]+nums_str[j]) and i!=j:
                    temp=nums_str[i]
                    nums_str[i]=nums_str[j]
                    nums_str[j]=temp
        
        no=''.join(nums_str)
        if all(char == '0' for char in no):
            return '0'
        
        return no

      








