class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=[]
        lo=[]
        l=title.split()
        print(l)
        for i in l:
            print(len(i))
            if len(i)>2:
                lo.append(i.capitalize())
            else:
                lo.append(i.lower())
        print(lo)

        s=" ".join(lo)
        print(s)
        return s