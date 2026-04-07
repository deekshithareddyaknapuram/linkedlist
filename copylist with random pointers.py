class Node:
    def __init__(self,x):
        self.val=x
        self.next=None
        self.random=None
def build_list(v,r):
    n=len(v)
    nodes=[Node(v[i])for i in range(n)]
    for i in range(n-1):
        nodes[i].next=nodes[i+1]
    for i in range(n):
        if r[i]!=-1:
            nodes[i].random=nodes[r[i]]
    return nodes[0] if n>0 else None
def copyRandomList(head):
    if not head:
        return None
    curr=head
    while curr:
        new=Node(curr.val)
        new.next=curr.next
        curr.next=new
        curr=new.next
    curr=head
    while curr:
        if curr.random:
            curr.next.random=curr.random.next
        curr=curr.next.next
    curr=head
    dummy=Node(0)
    copy_curr=dummy
    while curr:
        copy=curr.next
        curr.next=copy.next
        copy_curr.next=copy
        copy_curr=copy
        curr=curr.next
    return dummy.next
def print_list(head):
    curr=head
    while curr:
        print(curr.val,(curr.random.val if curr.random else -1),end=" ")
        curr=curr.next
    print()
n=int(input())
v=list(map(int,input().split()))
r=list(map(int,input().split()))
head=build_list(v,r)
print_list(head)
copy=copyRandomList(head)
print_list(copy)