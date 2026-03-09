class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def add(l1,l2):
    dummy=Node(0)
    temp=dummy
    carry=0
    while l1 or l2 or carry:
        val1=l1.data if l1 else 0
        val2=l2.data if l2 else 0
        total=val1+val2+carry
        carry=total//10
        digit=total%10
        temp.next=Node(digit)
        temp=temp.next
        if l1:
            l1=l1.next
        if l2:
            l2=l2.next
    return dummy.next

def build(arr):
    head=None
    temp=None
    for i in arr:
        new=Node(i)
        if head is None:
            head=new
            temp=head
        else:
            temp.next=new
            temp=temp.next
    return head

def printLL(head):
    while head:
        print(head.data,end=" ")
        head=head.next
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=build(l1)
l2=build(l2)
ans=add(l1,l2)

printLL(ans)