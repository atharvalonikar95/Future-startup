class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        
        for i in s:
            if i.isdigit()==True:
                l.append(int(i))
        
        l=set(l)
        l=list(l)
        l=sorted(l)
        print(l)

        if len(l)>=2:
            return l[-2]
        else :
            return -1 