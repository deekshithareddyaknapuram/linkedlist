class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def ispalindrome(head):
    if not head or not head.next:
        return True
    fast=head
    slow=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    prev=None
    curr=slow
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node

    first=head
    second=prev
    while second:
        if first.data!=second.data:
            return False
        first=first.next
        second=second.next
    return True
def createll(arr):
    head=Node(arr[0])
    temp=head
    for i in range (1,len(arr)):
        temp.next=Node(arr[i])
        temp=temp.next
    return head
arr=list(map(int,input().split()))
head=createll(arr)
if ispalindrome(head):
    print("palindrome")
else:
    print("Not palindrome")

    