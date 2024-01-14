class solution:
    

    def firstocc(self,needle):
        haystack=input("haystack: ")
        

        if needle in haystack:
            return haystack.find(needle)

        if needle not in haystack:
            return -1
needle=input("needle: ")
print(solution().firstocc(needle))
    