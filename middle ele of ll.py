class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def middle(head):
    fast=head
    slow=head
    prev=None
    while fast!=None and fast.next!=None:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    if fast is None:
        return prev,slow
    else:
        return slow,None
    

def printll(head):
    temp=head
    while temp:
        print(temp.data,end=" ")
        temp=temp.next
    print(None)
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
m1,m2=middle(head)
if m2:
    print(m1.data,m2.data)
else:
    print(m1.data)
    

