class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

def insert_before_head(head,val):
    new_node=Node(val)

    if head is None:
        head=new_node
        return head

    new_node.next=head
    head.prev=new_node
    head=new_node

    return head
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

val=int(input())

head=insert_before_head(head,val)

temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print("None")