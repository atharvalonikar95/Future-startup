list1=[]

while True:
   
    ip=int(input('''
             1 push 
             2 pop
             3 peek
             4 display
             5 exit
            "Enter your choice"
             '''))


    if ip==1:
        i=int(input("enter element"))
        list1.append(i)
    elif ip==2:
        if len(list1)==0:
            print("stack is empty")
        else:
            print(list1.pop())
    elif ip==3:
        if len(list1)==0:
            print("empty")
        print(list1[-1])
    elif ip==4:
        print(list1)
    elif ip==5:
        break
    else:
        print("please enter valid operation")
