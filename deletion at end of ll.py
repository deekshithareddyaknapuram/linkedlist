class Node:
    def __init__(self,data):
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
        temp=temp.next
if head is None:
    pass
elif head.next is None:
    head=None
else:
    temp=head
    # while temp.next.next:
    while temp.next is not None and temp.next.next is not None:
        temp=temp.next
    temp.next=None
temp=head
while temp:
    print(temp.data,end=" ->")
    temp=temp.next
print('None')





       
