class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def loopll(head):
    slow=head
    fast=head 
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            return True
    return False
def printll(head):
    temp=head
   
    while temp:
        print(temp.data,end=" ")
        temp=temp.next
    print("None")
n=int(input())
head=None
temp=None
for _ in range(n):
    val=int(input())
    new_node=Node(val)
    if head is None:

        head=new_node
        temp=head
    else:
        temp.next=new_node
        temp=temp.next


head=loopll(head)


print(head)
