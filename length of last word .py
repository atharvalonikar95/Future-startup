s=input("Enter string : ")
n=len(s)
count=0
for i in range(n-1,0,-1):
    if s[i]!=" ":
        count+=1
    elif count>0:
        break

print(count)

       