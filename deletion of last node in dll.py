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
while temp.next is not None:
    temp=temp.next
prev=temp.prev
prev.next=None
temp.prev=None
temp=head
while temp:
    print(temp.data,end=" ->")
    temp=temp.next
print('none')
