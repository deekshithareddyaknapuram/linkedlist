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
k=int(input())
c=1
temp=head
while temp is not None and c<k:
    temp=temp.next
    c+=1
   
   
if head is None:
    pass
elif temp.prev is None:
    temp.next
    if head is not None:
        head.prev=None
elif temp.next is None:
    temp.prev.next=None
else:
    temp.prev.next=temp.next
    temp.next.prev=temp.prev
temp=head    
while temp:
    print(temp.data,end=" ->")
    temp=temp.next
print('none')

