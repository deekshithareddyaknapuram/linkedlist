class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None


def insert_kth(head,val,k):
    new_node=Node(val)
    if k==1:
        new_node.next=head
        if head:
            head.prev=new_node
        return new_node
    temp=head
    count=1
    while temp and count<k-1:
        temp=temp.next
        count+=1

    if temp is None:
        return head

    new_node.next=temp.next
    new_node.prev=temp

    if temp.next:
        temp.next.prev=new_node

    temp.next=new_node

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
k=int(input())

head=insert_kth(head,val,k)

temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print("None")