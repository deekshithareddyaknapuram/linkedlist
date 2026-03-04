class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input('enter how many nums should be inserted'))
head=None
temp=None
for i in range(n):
    val=int(input('enter the nums'))
    new_node=Node(val)
    if head is None:
        head=new_node
        temp=head
    else:
        temp.next=new_node
        temp=temp.next
ele=int(input('what num should be inserted'))
k=int(input('where to insert the number'))
new_node=Node(ele)
if k==1:
    new_node.next=head
    head=new_node
else:
    temp=head
    c=1
    while c<k-1 and temp.next is not None:
        temp=temp.next
        c+=1
    new_node.next=temp.next
    temp.next=new_node
temp=head

temp=head
while temp:
    print(temp.data,end=" ->")
    temp=temp.next
print('None')