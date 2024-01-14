class solution:
    def diff(self,t):
        s=input("string s is :")
        for i in t:
            if i not in s:
                return i 
t=input("enter string t :")
obj1=solution()
print(obj1.diff(t))