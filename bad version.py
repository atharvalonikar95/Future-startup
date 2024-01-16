versions={}



k=int(input("enter number of versions"))
for i in range(k):
    ele=int

for i in range(k):
        key=int(input("enter key : "))
        value=bool(input("enter value : ").lower() == 'true')
        versions[key]=value

n=versions.__len__()


versions=dict(sorted(versions.items()))



def firstbad():
   if len(versions)==1:
       return versions[1]
   for i in range(n,-1,-1):
        if versions[i]==True and versions[i-1]==False:
            return i
        
     
print(firstbad())




