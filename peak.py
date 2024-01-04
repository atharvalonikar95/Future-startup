class solution:
    def peak(self,nums):
        
        n=len(nums)
        if n==1:
            return 0
        for i in range (n):
            if i==0 and nums[i]>nums[i+1]:
                return i
            elif i==n-1 and nums[i]>nums[i-1]:
                return i
            elif nums[i-1]<nums[i]>nums[i+1]:
                return i
nums=[]
k=int(input("enter number of elements :"))
for i in range (k):
    ele=int(input())
    nums.append(ele)
   

print("peak element is",solution().peak(nums))

