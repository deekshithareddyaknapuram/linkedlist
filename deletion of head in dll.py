class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
n=int(input())
head=None
temp=None
for i in range(n):
    val=int(input())
    new_node=Node(val)
    if head is None:
        head=new_node
        temp=head
    else:
        temp.next=new_node
        new_node.prev=temp
        temp=new_node
if head is not None:
    head=head.next
    if head is not None:
        head.prev=None
temp=head
while temp:
    print(temp.data,end=" ->")
    temp=temp.next
print('none')
