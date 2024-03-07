roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s=input("Enter roman number: ")
n=len(s)
ans=0
for i in range(n):
    if i<n-1 and roman[s[i]]<roman[s[i+1]]:
        ans=ans-roman[s[i]]
    else:
        ans=ans+roman[s[i]]
print("numeric value of above Roman number",s,"is",ans)

    