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
temp=head
while temp is not None:
   temp.prev,temp.next=temp.next,temp.prev
   head=temp
   temp=temp.prev
temp=head
while temp:
    print(temp.data,end=" ")
    temp=temp.next

