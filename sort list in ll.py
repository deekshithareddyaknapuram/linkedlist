class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def getmid(head):
    slow=head
    fast=head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
def mergek(l1,l2):
    dummy=Node(0)
    tail=dummy
    while l1 and l2:
        if l1.data<l2.data:
            tail.next=l1
            l1=l1.next
        else:
            tail.next=l2
            l2=l2.next
        tail=tail.next
    tail.next=l1 if l1 else l2
    return dummy.next
def sort(head):
    if not head or not head.next:
        return head
    mid=getmid(head)
    right=mid.next
    mid.next=None
    left=head
    left=sort(left)
    right=sort(right)
    return mergek(left,right)
def printll(head):
    
    temp=head
    while temp:
        print(temp.data,end=" ")
        temp=temp.next
    print('None')
n=int(input())
head=None
temp=None
for _ in range(n):
    val=int(input())
    new_node=Node(val)
    if not head:
        head=new_node
        temp=head
    else:
        temp.next=new_node
        temp=temp.next
head=sort(head)
printll(head)


