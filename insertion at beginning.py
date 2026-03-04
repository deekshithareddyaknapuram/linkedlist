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
ele=int(input())
new_node=Node(ele)
new_node.next=head
head=new_node
temp=head
while temp:
    print(temp.data,end=" ->")
    temp=temp.next
print('None')