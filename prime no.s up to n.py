import math
n=int(input("enter number: "))
count=0
for i in range (n):
    
    if i<=1:
        pass
        
    elif i==2:
        count+=1
    elif i%2==0:
        pass
    else:
        is_prime = True
        for j in range(3,int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                is_prime = False
                
                break  
        if is_prime:
            
            count += 1
print("the number of prime numbers encountered are ",count,"upto number ",n)
        

    
