# list1=[]
# class ListNode:
#     def __init__(self,val,next=None) :
#         self.val=val
#         self.next=next

# class linkedlist:
#     def __init__(self,head=None):
#         self.head=head 
    
#     def insert(self,val):
#         node=ListNode(val)
#         if self.head is None:
#             self.head=node
#             return
#         curr =self.head
#         while True:
#             if curr.next is None:
#                 curr.next=node
#                 break
#             curr=curr.next
#     def printlinkedlist(self):
#         curr=self.head
#         while curr is not None:
#             print(curr.val,"->",end=" ")
#             list1.append(curr.val)
#             list1.sort()
            
#             curr=curr.next
#         print("none")


# ll1=linkedlist()
# ll1.insert(1)
# ll1.insert(5)
# ll1.printlinkedlist()

# ll2=linkedlist()
# ll2.insert(9)
# ll2.insert(4)
# ll2.printlinkedlist()
# print(list1)


class listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class linkedlist:
    def __init__(self,head) :
        self.head=head
    
    def insert(self,val):
        node=listnode(val)

        if self.head is None:
            self.head= node
            return
        
        curr=self.head
        while True:
            if curr.next is None:
                curr.next=node
                break

    def remove(self,val):
        if self.head is None:
            print("linkedlist is empty")
        
        
    def print (self):
        curr=self.head
        while curr is not None:
            print( curr.next,"->",end=" ")
            curr=curr.next


                