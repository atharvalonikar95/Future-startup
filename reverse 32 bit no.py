class solution:
    
    def reverse(self,n):
        num=[]
        
        if n not in range(-2**31,2**31 ) or n==0:
            return 0
        
        sign=1
        if n<0:
            sign=-1
        n=abs(n)
            

        while n!=0:
            rem=n%10
            num.append(rem)
            n//=10
        rev=''.join(str(digit) for digit in num[::1])
        m = sign * int(rev)

        if m not in range(-2**31, 2**31):
            return 0

        
        
        return sign * int(rev)
k=int(input("Enter number: "))       
print("the reverse of number",k,"is",solution().reverse(k))

